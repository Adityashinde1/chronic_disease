import os
import sys
from kidney_disease.exception import kidneyDiseaseException
from kidney_disease.util.util import load_object
import pandas as pd


class KidneyDiseaseData:

    def __init__(self,age: float, bp: float, sg: float, al: float, su: float, rbc: int, pc: int, pcc: int, ba: int, bgr: float, bu: float,
                 sc: float, sod: float, pot: float, hemo: float, pcv: float, wc: float, rc: float, htn: int, dm: int, cad: int, appet: int,
                 pe: int, ane: int):
        try:
            self.age = age
            self.bp = bp
            self.sg = sg
            self.al = al
            self.su = su
            self.rbc = rbc
            self.pc = pc
            self.pcc = pcc
            self.ba = ba
            self.bgr = bgr
            self.bu = bu
            self.sc = sc
            self.sod = sod
            self.pot = pot
            self.hemo = hemo
            self.pcv = pcv
            self.wc = wc
            self.rc = rc
            self.htn = htn
            self.dm = dm
            self.cad = cad
            self.appet = appet
            self.pe = pe
            self.ane = ane

        except Exception as e:
            raise kidneyDiseaseException(e, sys) from e

    def get_kidney_disease_input_data_frame(self):

        try:
            kidney_disease_input_dict = self.get_kidney_disease_data_as_dict()
            return pd.DataFrame(kidney_disease_input_dict)
        except Exception as e:
            raise kidneyDiseaseException(e, sys) from e

    def get_kidney_disease_data_as_dict(self):
        try:
            input_data = {"age": [self.age], "bp": [self.bp], "sg": [self.sg], "al": [self.al], "su": [self.su],"rbc": [self.rbc],
            "pc": [self.pc],"pcc": [self.pcc],"ba": [self.ba],"bgr": [self.bgr],"bu": [self.bu],"sc": [self.sc], "sod": [self.sod],
            "pot": [self.pot],"hemo": [self.hemo],"pcv": [self.pcv],"wc": [self.wc], "rc": [self.rc],"htn": [self.htn],"dm": [self.dm],
            "cad": [self.cad], "appet": [self.appet],"pe": [self.pe],"ane": [self.ane]}
            return input_data
        except Exception as e:
            raise kidneyDiseaseException(e, sys)


class KidneyDiseasePredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise kidneyDiseaseException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise kidneyDiseaseException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            median_kidneyDisease_value = model.predict(X)
            return median_kidneyDisease_value
        except Exception as e:
            raise kidneyDiseaseException(e, sys) from e