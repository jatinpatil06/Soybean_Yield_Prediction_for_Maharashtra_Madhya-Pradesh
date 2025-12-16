from pydantic import BaseModel, Field, field_validator
from typing import Literal

class YieldInput(BaseModel):
    AREA : float
    PS : float
    TS : float
    QV2M : float
    WS2M : float
    CLOUD_AMT : float
    ALLSKY_SFC_SW_DWN : float
    ALLSKY_SFC_PAR_TOT : float 
    RH2M : float
    GWETROOT : float
    T2M_RANGE : float 
    nitrogen : Literal["Low", "Medium", "High"] = Field(alias = 'Nitrogen(N)') 
    phosphorous : Literal["Low", "Medium", "High"] = Field(alias = 'Phosphorous(P)') 
    potassium : Literal["Low", "Medium", "High"] = Field(alias = 'Potassium(K)') 
    soil_type : Literal["Black", "Mixed Red & Black", "Red", "Alluvial"] = Field(alias = 'Soil Type')  
    soil_depth : Literal["100-300", "50-100", "25-50"] = Field(alias = 'Soil Depth') 

    #-----Validators-----
    @field_validator("AREA", "PS", "TS", "QV2M", "WS2M", "CLOUD_AMT", "ALLSKY_SFC_SW_DWN", "ALLSKY_SFC_PAR_TOT", "RH2M", "GWETROOT", "T2M_RANGE")
    @classmethod
    def non_negative(cls, v):
        if v < 0:
            raise ValueError("Value must be non-negative!")
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
            "AREA": 3.427118,
            "PS": 95.633212,
            "TS": 27.156435,
            "QV2M": 10.602373,
            "WS2M": 2.630678,
            "CLOUD_AMT": 43.384391,
            "ALLSKY_SFC_SW_DWN": 19.615255,
            "ALLSKY_SFC_PAR_TOT": 9.507120,
            "RH2M": 51.391027,
            "GWETROOT": 0.644237,
            "T2M_RANGE": 37.446608,
            "Nitrogen(N)": "Low",
            "Phosphorous(P)": "Low",
            "Potassium(K)": "High",
            "Soil Type": "Black",
            "Soil Depth": "100-300"
            }
        }

