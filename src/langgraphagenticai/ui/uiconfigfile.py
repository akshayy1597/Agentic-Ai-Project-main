from configparser import ConfigParser   #whenever we have this config file the ConfigParser is a class which will parse the entire text file and will give us the key value pairs

class Config:
    def __init__(self,config_file="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config=ConfigParser()  
        self.config.read(config_file)   #this will be able to read the entire config file which we are giving as input

    def get_llm_options(self):  #this is to read the LLM function from the config file 
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")    #DEFAULT is the root node specified in the .ini file 
                                                                        #, : is the separator so as to choose between the LLM options given in the .ini file
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")    #by .get we should be able to read it in key value pair format

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")

