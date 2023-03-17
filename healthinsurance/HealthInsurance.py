import pandas as pd
import pickle

class HealthInsurance:
    
    def __init__(self):
        self.home_path = ''
        self.scaler_age = pickle.load(open(self.home_path + 'artifacts/scaler_age.pkl', 'rb'))
        self.scaler_vintage = pickle.load(open(self.home_path + 'artifacts/scaler_vintage.pkl', 'rb'))
        self.scaler_annual_premium = pickle.load(open(self.home_path + 'artifacts/scaler_annual_premium.pkl', 'rb'))
        self.ohe_encoder_gender = pickle.load(open(self.home_path + 'artifacts/ohe_encoder_gender.pkl', 'rb'))
        self.ohe_encoder_vehicle_age = pickle.load(open(self.home_path + 'artifacts/ohe_encoder_vehicle_age.pkl', 'rb'))
        self.ohe_encoder_vehicle_damage = pickle.load(open(self.home_path + 'artifacts/ohe_encoder_vehicle_damage.pkl', 'rb'))
        self.frequency_encode_policy_sales_channel = pickle.load(open(self.home_path + 'artifacts/frequency_encode_policy_sales_channel.pkl', 'rb'))
        self.target_encode_region_code = pickle.load(open(self.home_path + 'artifacts/target_encode_region_code.pkl', 'rb'))
        
    def _ohe(self, data, col, encoder):
        ohe_encoded_columns = encoder.transform(data[[col]])
        ohe_encoded_dataframe = pd.DataFrame(ohe_encoded_columns, columns=encoder.get_feature_names_out())
        ohe_encoded_dataframe.reset_index(drop=True, inplace=True)
        data = pd.concat([data, ohe_encoded_dataframe], axis=1)
        data = data.drop(col, axis=1)
        
        return data
        
    def data_cleaning(self, df1):
        new_cols = [col.lower() for col in df1.columns]
        df1.columns = new_cols
        
        return df1
        
        
    def data_preparation(self, df2):
        df2['age'] = self.scaler_age.transform(df2[['age']].values)
        df2['vintage'] = self.scaler_vintage.transform(df2[['vintage']].values)
        df2['annual_premium'] = self.scaler_annual_premium.transform(df2[['annual_premium']].values)
        df2 = self._ohe(df2, 'gender', self.ohe_encoder_gender)
        df2 = self._ohe(df2, 'vehicle_age', self.ohe_encoder_vehicle_age)
        df2 = self._ohe(df2, 'vehicle_damage', self.ohe_encoder_vehicle_damage)
        df2['policy_sales_channel'] = df2['policy_sales_channel'].map(self.frequency_encode_policy_sales_channel)
        df2['region_code'] = df2['region_code'].map(self.target_encode_region_code)
        
        return df2
    
    
    def data_selection(self, df3):
        return df3[['vintage', 'annual_premium', 'age', 'region_code', 
                    'policy_sales_channel', 
                    'vehicle_damage_Yes', 'vehicle_damage_No']]
    
    
    def get_prediction(self, model, original_data, prediction_data):
        ypred_proba = model.predict_proba(prediction_data)
        original_data['prediction'] = ypred_proba[:, 1]
        
        return original_data.to_json(orient='records')   