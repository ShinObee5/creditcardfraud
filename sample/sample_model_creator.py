import pickle


class Model():
    def __repr__(self):
        return f"The model imitates xgboost"
    
    def predict(self,string):
        return f"Value Predicted for String as {string}"

model = Model()
with open('model.pkl','wb') as f:
    pickle.dump(model,f)