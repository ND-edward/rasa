# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import pandas as pd
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

product_df = pd.read_excel("C:/Users/Techteam/Desktop/gratus_content/rasa/product.xlsx")
treatment_df = pd.read_excel("C:/Users/Techteam/Desktop/gratus_content/rasa/treatment.xlsx")

class ValidateSkinForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_skin_form"

    async def required_slots(
        self,
        domain_slots: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[Text]:
        updated_slots = domain_slots.copy()

        if tracker.get_slot("first_skin_type") == '唔知' or tracker.get_slot("inform_skin_problem") == '防曬':
            updated_slots.remove("product_or_treatment")
        
        return updated_slots

    # def validate_first_skin_type(
    #     self,
    #     slot_value: Any,
    #     dispatcher: "CollectingDispatcher",
    #     tracker: "Tracker",
    #     domain: "DomainDict",
    # ) -> Dict[Text, Any]:

    #     skin_type = tracker.get_slot("first_skin_type")
    #     message = f"確認您嘅膚質為{skin_type}"

    #     dispatcher.utter_message(text=message)

    #     return {"first_skin_type": skin_type}

class ActionCarousel(Action):
    def name(self) -> Text:
        return "action_product_treatment_carousel"

    def run(
        self, 
        dispatcher, 
        tracker: Tracker, 
        domain: "DomainDict"
    ) -> List[Dict[Text, Any]]:
        
        moisture_mixed_product = {
            "type" : "template",
            "payload":{
                "template_type":"generic",
                "elements":[
                    {
                        "title": "全效維他命B5補濕精華",
                        "image_url": "https://gratushk.oss-cn-hongkong.aliyuncs.com/gratus/PublicImages/ND/Upload/Internal/e090a7a1-cc28-aa30-31c1-f9824a6c511c-1_Bicelle_Hydra_B5_gel_Aqua_Rejuvenation_Unique_combination_of_3_active_Peptides_immensely_rejuvenates_and_locks_moisture_in_skin.jpg",
                        "buttons":[
                            {
                            "title": "詳情",
                            "url":"https://www.gratus.com.hk/product/detail/297/358",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "全效維他命 B5 補濕霜",
                        "image_url": "https://gratushk.oss-cn-hongkong.aliyuncs.com/gratus/PublicImages/ND/Upload/Internal/0cb4b772-e98e-9bcd-f57c-a567bc500abe-1_Bicelle_HydraB5Cream_Moisturizing.jpg",
                        "buttons":[
                            {
                            "title": "詳情",
                            "url":"https://www.gratus.com.hk/product/detail/295/356",
                            "type": "web_url"
                            }
                        ] 
                    }
                ]
            }
        }
        moisture_oil_product = {
            "type" : "template",
            "payload":{
                "template_type":"generic",
                "elements":[
                    {
                        "title": "活肌修復霜",
                        "image_url": "https://oss.gratus.com.hk/gratus/PublicImages/ND/Upload/Internal/c291b22a-7ef8-96f0-ee2a-0e3c946108f2-Gelcream_1000x1000.png",
                        "buttons":[
                            {
                            "title": "詳情",
                            "url":"https://www.gratus.com.hk/product/detail/318",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "全效維他命 B5 補濕霜",
                        "image_url": "https://gratushk.oss-cn-hongkong.aliyuncs.com/gratus/PublicImages/ND/Upload/Internal/0cb4b772-e98e-9bcd-f57c-a567bc500abe-1_Bicelle_HydraB5Cream_Moisturizing.jpg",
                        "buttons":[
                            {
                            "title": "詳情",
                            "url":"https://www.gratus.com.hk/product/detail/295/356",
                            "type": "web_url"
                            }
                        ] 
                    }
                ]
            }
        }
        moisture_dry_product = {
            "type" : "template",
            "payload":{
                "template_type":"generic",
                "elements":[
                    {
                        "title": "全效維他命 B5 補濕面膜",
                        "image_url": "https://oss.gratus.com.hk/gratus/PublicImages/ItemType/Hydra_B5_Cream_Mask_50g_1000px.png",
                        "buttons":[
                            {
                            "title": "詳情",
                            "url":"https://www.gratus.com.hk/product/detail/296",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "全效維他命 B5 補濕霜",
                        "image_url": "https://gratushk.oss-cn-hongkong.aliyuncs.com/gratus/PublicImages/ND/Upload/Internal/0cb4b772-e98e-9bcd-f57c-a567bc500abe-1_Bicelle_HydraB5Cream_Moisturizing.jpg",
                        "buttons":[
                            {
                            "title": "詳情",
                            "url":"https://www.gratus.com.hk/product/detail/295/356",
                            "type": "web_url"
                            }
                        ] 
                    }
                ]
            }
        }
        moisture_mixed_treatment = {
            "type" : "template",
            "payload":{
                "template_type":"generic",
                "elements":[
                    {
                        "title": "全新升級HGF倍效激活細胞增生療程",
                        "image_url": "https://oss.gratus.com.hk/gratus/PublicImages/ItemType/Entry%20Point%202.3.png",
                        "buttons":[
                            {
                            "title": "詳情",
                            "url":"https://www.reenex.com.hk/zh/treatment-hgf",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
            }
        }
        moisture_oil_treatment = {
            "type" : "template",
            "payload":{
                "template_type":"generic",
                "elements":[
                    {
                        "title": "全新升級HGF倍效激活細胞增生療程",
                        "image_url": "https://oss.gratus.com.hk/gratus/PublicImages/ItemType/Entry%20Point%202.3.png",
                        "buttons":[
                            {
                            "title": "詳情",
                            "url":"https://www.reenex.com.hk/zh/treatment-hgf",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
            }
        }        
        moisture_dry_treatment = {
            "type" : "template",
            "payload":{
                "template_type":"generic",
                "elements":[
                    {
                        "title": "全新升級HGF倍效激活細胞增生療程",
                        "image_url": "https://oss.gratus.com.hk/gratus/PublicImages/ItemType/Entry%20Point%202.3.png",
                        "buttons":[
                            {
                            "title": "詳情",
                            "url":"https://www.reenex.com.hk/zh/treatment-hgf",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
            }
        }          
        
        suncare_mixed_product = {
            "type" : "template",
            "payload":{
                "template_type":"generic",
                "elements":[
                    {
                        "title": "360° 溫和礦物防曬乳 SPF50",
                        "image_url": "https://oss.gratus.com.hk/gratus/PublicImages/ND/Upload/Internal/b8bf325e-df6f-dc84-6170-49f694d43bc8-mineral%201000x1000.png",
                        "buttons":[
                            {
                            "title": "詳情",
                            "url":"https://www.gratus.com.hk/product/detail/1499/1505",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
            }
        } 
        suncare_oil_product = {
            "type" : "template",
            "payload":{
                "template_type":"generic",
                "elements":[
                    {
                        "title": "360° 清爽控油防曬乳 SPF50",
                        "image_url": "https://oss.gratus.com.hk/gratus/PublicImages/ND/Upload/Internal/b19a7f44-f8f9-38b5-2bc2-bd3235933955-gel%20oil%20free%201000x1000.png",
                        "buttons":[
                            {
                            "title": "詳情",
                            "url":"https://www.gratus.com.hk/product/detail/1498/1504",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
            }
        } 
        suncare_dry_product = {
            "type" : "template",
            "payload":{
                "template_type":"generic",
                "elements":[
                    {
                        "title": "360° 水感補濕防曬乳 SPF 50+",
                        "image_url": "https://oss.gratus.com.hk/gratus/PublicImages/ND/Upload/Internal/b8bf325e-df6f-dc84-6170-49f694d43bc8-mineral%201000x1000.png",
                        "buttons":[
                            {
                            "title": "詳情",
                            "url":"https://www.gratus.com.hk/product/detail/1499/1505",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
            }
        } 

        if tracker.get_slot("product_or_treatment") == "產品":
            if tracker.get_slot("inform_skin_problem") == '保濕' or tracker.get_slot("inform_skin_problem") == '乾燥':
                if tracker.get_slot("first_skin_type") == "混合性":
                    dispatcher.utter_message(attachment=moisture_mixed_product)
                elif tracker.get_slot("first_skin_type") == "油性":
                    dispatcher.utter_message(attachment=moisture_oil_product)
                elif tracker.get_slot("first_skin_type") == "乾性":
                    dispatcher.utter_message(attachment=moisture_dry_product)
        
        elif tracker.get_slot("product_or_treatment") == "療程":
            if tracker.get_slot("inform_skin_problem") == '保濕' or tracker.get_slot("inform_skin_problem") == '乾燥':
                if tracker.get_slot("first_skin_type") == "混合性":
                    dispatcher.utter_message(attachment=moisture_mixed_treatment)
                elif tracker.get_slot("first_skin_type") == "油性":
                    dispatcher.utter_message(attachment=moisture_oil_treatment)
                elif tracker.get_slot("first_skin_type") == "乾性":
                    dispatcher.utter_message(attachment=moisture_dry_treatment)
        
        elif tracker.get_slot("inform_skin_problem") == '防曬':
            if tracker.get_slot("first_skin_type") == "混合性":
                dispatcher.utter_message(attachment=suncare_mixed_product)
            elif tracker.get_slot("first_skin_type") == "油性":
                dispatcher.utter_message(attachment=suncare_oil_product)
            elif tracker.get_slot("first_skin_type") == "乾性":
                dispatcher.utter_message(attachment=suncare_dry_product)
        
        else:
            dispatcher.utter_message("[識別肌膚](https://www.greenvines.com.tw/pages/blog-self-skin-type-test)")
        
        return []

class MoreOptionsAction(Action):
    def name(self) -> Text:
        return "action_inquiry_more_details"

    def run(
        self, 
        dispatcher, 
        tracker: Tracker, 
        domain: "DomainDict"
    ) -> List[Dict[Text, Any]]:
        text = "仲有冇嘢想了解呢?"
        product_or_treatment = tracker.get_slot('product_or_treatment')

        # Below script is suitable for all skin_problem except 防曬
        buttons = []
        # Add the required buttons no matter the product_or_treatment slot == "療程" or "產品"
        buttons.append(
            {"title":f"推薦{product_or_treatment}有咩功效?", "payload":"/inquiry_product_treatment_effect"}) 

        if tracker.get_slot("product_or_treatment") == "療程":
            dispatcher.utter_message(text=text, buttons=buttons)

        elif tracker.get_slot("product_or_treatment") == "產品":
            buttons.extend([
                {"title":"推薦產品建議用法配搭", "payload":"/recommend_product_usage"},
                {"title":"推薦產品庫存", "payload":"/inquiry_product_quantity"}])
            dispatcher.utter_message(text=text, buttons=buttons)

        # Below script is suitable for 防曬 only
        elif tracker.get_slot("inform_skin_problem") == '防曬':
            suncare_buttons = []

            suncare_buttons.extend([
                {"title":"推薦產品有咩功效?", "payload":"/inquiry_product_treatment_effect"},
                {"title":"推薦產品庫存", "payload":"/inquiry_product_quantity"}])
            dispatcher.utter_message(text=text, buttons=suncare_buttons)
        
        else:
            dispatcher.utter_message(text=text)

        return []

class IntroProductTreatmentAction(Action):
    def name(self) -> Text:
        return "action_intro_product_treatment_effect"

    def run(
        self, 
        dispatcher, 
        tracker: Tracker, 
        domain: "DomainDict"
    ) -> List[Dict[Text, Any]]:

        moisture_product_df = product_df[product_df.category == "moisture"]
        moisture_treatment_df = treatment_df[treatment_df.category == "moisture"]

        suncare_product_df = product_df[product_df.category == "suncare"]

        if tracker.get_slot("product_or_treatment") == "產品":
            if tracker.get_slot("inform_skin_problem") == '保濕' or tracker.get_slot("inform_skin_problem") == '乾燥':
                print('inform_skin_problem')

                if tracker.get_slot("first_skin_type") == "混合性":

                    mixed_skin_product_df = moisture_product_df[moisture_product_df.skin_type == "mixed"]
                    mixed_product = dict(zip(mixed_skin_product_df['product'], mixed_skin_product_df.effect))
                    message = f'1{list(mixed_product.keys())[0]}: {list(mixed_product.values())[0]}\n\n2️{list(mixed_product.keys())[1]}: {list(mixed_product.values())[1]}'
                    dispatcher.utter_message(text=message)
                
                elif tracker.get_slot("first_skin_type") == "油性":

                    oil_skin_product_df = moisture_product_df[moisture_product_df.skin_type == "oil"]
                    oil_product = dict(zip(oil_skin_product_df['product'], oil_skin_product_df.effect))
                    message = f'1️{list(oil_product.keys())[0]}: {list(oil_product.values())[0]}\n\n2️{list(oil_product.keys())[1]}: {list(oil_product.values())[1]}'
                    dispatcher.utter_message(text=message)

                elif tracker.get_slot("first_skin_type") == "乾性":
                
                    dry_skin_product_df = moisture_product_df[moisture_product_df.skin_type == "dry"]
                    dry_product = dict(zip(dry_skin_product_df['product'], dry_skin_product_df.effect))
                    message = f'1️{list(dry_product.keys())[0]}: {list(dry_product.values())[0]}\n\n2️{list(dry_product.keys())[1]}: {list(dry_product.values())[1]}'
                    dispatcher.utter_message(text=message)
        
        elif tracker.get_slot("product_or_treatment") == "療程":
            if tracker.get_slot("inform_skin_problem") == '保濕' or tracker.get_slot("inform_skin_problem") == '乾燥':

                if tracker.get_slot("first_skin_type") == "混合性":

                    mixed_skin_treatment_df = moisture_treatment_df[moisture_treatment_df.skin_type == "mixed"]
                    mixed_treatment = dict(zip(mixed_skin_treatment_df.treatment, mixed_skin_treatment_df.effect))
                    message = f'1️⃣{list(mixed_treatment.keys())[0]}: {list(mixed_treatment.values())[0]}'
                    dispatcher.utter_message(text=message)

                elif tracker.get_slot("first_skin_type") == "油性":
                    
                    oil_skin_treatment_df = moisture_treatment_df[moisture_treatment_df.skin_type == "oil"]
                    oil_treatment = dict(zip(oil_skin_treatment_df.treatment, oil_skin_treatment_df.effect))
                    message = f'1️⃣{list(oil_treatment.keys())[0]}: {list(oil_treatment.values())[0]}'
                    dispatcher.utter_message(text=message)

                elif tracker.get_slot("first_skin_type") == "乾性":
                
                    dry_skin_treatment_df = moisture_treatment_df[moisture_treatment_df.skin_type == "dry"]
                    dry_treatment = dict(zip(dry_skin_treatment_df.treatment, dry_skin_treatment_df.effect))
                    message = f'1️⃣{list(dry_treatment.keys())[0]}: {list(dry_treatment.values())[0]}'
                    dispatcher.utter_message(text=message)
        
        elif tracker.get_slot("inform_skin_problem") == '防曬':
            if tracker.get_slot("first_skin_type") == "混合性":

                mixed_skin_product_df = suncare_product_df[suncare_product_df.skin_type == "mixed"]
                mixed_product = dict(zip(mixed_skin_product_df['product'], mixed_skin_product_df.effect))
                message = f'1️⃣{list(mixed_product.keys())[0]}: {list(mixed_product.values())[0]}'
                dispatcher.utter_message(text=message)
        
            elif tracker.get_slot("first_skin_type") == "油性":

                oil_skin_product_df = suncare_product_df[suncare_product_df.skin_type == "oil"]
                oil_product = dict(zip(oil_skin_product_df['product'], oil_skin_product_df.effect))
                message = f'1️⃣{list(oil_product.keys())[0]}: {list(oil_product.values())[0]}'
                dispatcher.utter_message(text=message)

            elif tracker.get_slot("first_skin_type") == "乾性":

                dry_skin_product_df = suncare_product_df[suncare_product_df.skin_type == "dry"]
                dry_product = dict(zip(dry_skin_product_df['product'], dry_skin_product_df.effect))
                message = f'1️⃣{list(dry_product.keys())[0]}: {list(dry_product.values())[0]}'
                dispatcher.utter_message(text=message)

        return []

class ProductRecommendUsageAction(Action):
    def name(self) -> Text:
        return "action_recommend_product_usage"

    def run(
        self, 
        dispatcher, 
        tracker: Tracker, 
        domain: "DomainDict"
    ) -> List[Dict[Text, Any]]:

        if tracker.get_slot("product_or_treatment") == "產品":
            if tracker.get_slot("inform_skin_problem") == '保濕' or tracker.get_slot("inform_skin_problem") == '乾燥':
                if tracker.get_slot("first_skin_type") == "混合性":

                    mixed_skin_product_df = product_df[product_df.skin_type == "mixed"]
                    mixed_product = dict(zip(mixed_skin_product_df['product'], mixed_skin_product_df.effect))
                    message = f'步驟1️⃣{list(mixed_product.keys())[0]}\n\n步驟2️⃣{list(mixed_product.keys())[1]}'
                    dispatcher.utter_message(text=message)
                
                elif tracker.get_slot("first_skin_type") == "油性":

                    oil_skin_product_df = product_df[product_df.skin_type == "oil"]
                    oil_product = dict(zip(oil_skin_product_df['product'], oil_skin_product_df.effect))
                    message = f'步驟1️⃣{list(oil_product.keys())[0]}\n\n步驟2️⃣{list(oil_product.keys())[1]}'
                    dispatcher.utter_message(text=message)

                elif tracker.get_slot("first_skin_type") == "乾性":

                    dry_skin_product_df = product_df[product_df.skin_type == "dry"]
                    dry_product = dict(zip(dry_skin_product_df['product'], dry_skin_product_df.effect))
                    message = f'步驟1️⃣{list(dry_product.keys())[0]}\n\n步驟2️⃣{list(dry_product.keys())[1]}'
                    dispatcher.utter_message(text=message)
        return []

class ProductQuantityAction(Action):
    def name(self) -> Text:
        return "action_product_quantity"

    def run(
        self, 
        dispatcher, 
        tracker: Tracker, 
        domain: "DomainDict"
    ) -> List[Dict[Text, Any]]:

        moisture_product_df = product_df[product_df.category == "moisture"]
        suncare_product_df = product_df[product_df.category == "suncare"]

        if tracker.get_slot("product_or_treatment") == "產品":
            if tracker.get_slot("inform_skin_problem") == '保濕' or tracker.get_slot("inform_skin_problem") == '乾燥':

                if tracker.get_slot("first_skin_type") == "混合性":
                    
                    mixed_skin_product_df = moisture_product_df[moisture_product_df.skin_type == "mixed"]
                    
                    # Products with stock
                    mixed_skin_product_have_stock_df = mixed_skin_product_df[mixed_skin_product_df.quantity > 0]
                    mixed_product_have_stock = dict(zip(mixed_skin_product_have_stock_df['product'], mixed_skin_product_have_stock_df.quantity))

                    have_stock_product_list = []
                    for i in range(len(mixed_product_have_stock)):
                        have_stock_product = f"{list(mixed_product_have_stock.keys())[i]} 現時仍有存貨 {list(mixed_product_have_stock.values())[i]} 件"
                        have_stock_product_list.append(have_stock_product)
                    have_stock_product = ", ".join(have_stock_product_list)

                    # Products without stock
                    mixed_skin_product_no_stock_df = mixed_skin_product_df[mixed_skin_product_df.quantity == 0]
                    no_stock_product_list = list(mixed_skin_product_no_stock_df['product'])
                    no_stock_product = ", ".join(no_stock_product_list)
                    no_stock_product = no_stock_product + " 仍未有存貨"

                    message = f'{have_stock_product}\n\n{no_stock_product}'

                    dispatcher.utter_message(text=message)
                
                elif tracker.get_slot("first_skin_type") == "油性":
                    
                    oil_skin_product_df = moisture_product_df[moisture_product_df.skin_type == "oil"]
                    
                    # Products with stock
                    oil_skin_product_have_stock_df = oil_skin_product_df[oil_skin_product_df.quantity > 0]
                    oil_product_have_stock = dict(zip(oil_skin_product_have_stock_df['product'], oil_skin_product_have_stock_df.quantity))

                    have_stock_product_list = []
                    for i in range(len(oil_product_have_stock)):
                        have_stock_product = f"{list(oil_product_have_stock.keys())[i]} 現時仍有存貨 {list(oil_product_have_stock.values())[i]} 件"
                        have_stock_product_list.append(have_stock_product)
                    have_stock_product = ", ".join(have_stock_product_list)

                    # Products without stock
                    oil_skin_product_no_stock_df = oil_skin_product_df[oil_skin_product_df.quantity == 0]
                    no_stock_product_list = list(oil_skin_product_no_stock_df['product'])
                    no_stock_product = ", ".join(no_stock_product_list)
                    no_stock_product = no_stock_product + " 仍未有存貨"

                    message = f'{have_stock_product}\n\n{no_stock_product}'

                    dispatcher.utter_message(text=message)

                elif tracker.get_slot("first_skin_type") == "乾性":

                    dry_skin_product_df = moisture_product_df[moisture_product_df.skin_type == "dry"]
                    
                    # Products with stock
                    dry_skin_product_have_stock_df = dry_skin_product_df[dry_skin_product_df.quantity > 0]
                    dry_product_have_stock = dict(zip(dry_skin_product_have_stock_df['product'], dry_skin_product_have_stock_df.quantity))

                    have_stock_product_list = []
                    for i in range(len(dry_product_have_stock)):
                        have_stock_product = f"{list(dry_product_have_stock.keys())[i]} 現時仍有存貨 {list(dry_product_have_stock.values())[i]} 件"
                        have_stock_product_list.append(have_stock_product)
                    have_stock_product = ", ".join(have_stock_product_list)

                    # Products without stock
                    dry_skin_product_no_stock_df = dry_skin_product_df[dry_skin_product_df.quantity == 0]
                    no_stock_product_list = list(dry_skin_product_no_stock_df['product'])
                    no_stock_product = ", ".join(no_stock_product_list)
                    no_stock_product = no_stock_product + " 仍未有存貨"

                    message = f'{have_stock_product}\n\n{no_stock_product}'

                    dispatcher.utter_message(text=message)

        elif tracker.get_slot("inform_skin_problem") == '防曬':
            if tracker.get_slot("first_skin_type") == "混合性":
                    
                mixed_skin_product_df = suncare_product_df[suncare_product_df.skin_type == "mixed"]
                    
                # Products with stock
                mixed_skin_product_have_stock_df = mixed_skin_product_df[mixed_skin_product_df.quantity > 0]
                mixed_product_have_stock = dict(zip(mixed_skin_product_have_stock_df['product'], mixed_skin_product_have_stock_df.quantity))

                have_stock_product_list = []
                for i in range(len(mixed_product_have_stock)):
                    have_stock_product = f"{list(mixed_product_have_stock.keys())[i]} 現時仍有存貨 {list(mixed_product_have_stock.values())[i]} 件"
                    have_stock_product_list.append(have_stock_product)
                have_stock_product = ", ".join(have_stock_product_list)

                # Products without stock
                mixed_skin_product_no_stock_df = mixed_skin_product_df[mixed_skin_product_df.quantity == 0]
                no_stock_product_list = list(mixed_skin_product_no_stock_df['product'])
                no_stock_product = ", ".join(no_stock_product_list)
                no_stock_product = no_stock_product + " 仍未有存貨"

                message = f'{have_stock_product}\n\n{no_stock_product}'

                dispatcher.utter_message(text=message)
                
            elif tracker.get_slot("first_skin_type") == "油性":
                    
                oil_skin_product_df = suncare_product_df[suncare_product_df.skin_type == "oil"]
                    
                # Products with stock
                oil_skin_product_have_stock_df = oil_skin_product_df[oil_skin_product_df.quantity > 0]
                oil_product_have_stock = dict(zip(oil_skin_product_have_stock_df['product'], oil_skin_product_have_stock_df.quantity))

                have_stock_product_list = []
                for i in range(len(oil_product_have_stock)):
                    have_stock_product = f"{list(oil_product_have_stock.keys())[i]} 現時仍有存貨 {list(oil_product_have_stock.values())[i]} 件"
                    have_stock_product_list.append(have_stock_product)
                have_stock_product = ", ".join(have_stock_product_list)

                # Products without stock
                oil_skin_product_no_stock_df = oil_skin_product_df[oil_skin_product_df.quantity == 0]
                no_stock_product_list = list(oil_skin_product_no_stock_df['product'])
                no_stock_product = ", ".join(no_stock_product_list)
                no_stock_product = no_stock_product + " 仍未有存貨"

                message = f'{have_stock_product}\n\n{no_stock_product}'

                dispatcher.utter_message(text=message)

            elif tracker.get_slot("first_skin_type") == "乾性":

                dry_skin_product_df = suncare_product_df[suncare_product_df.skin_type == "dry"]
                
                # Products with stock
                dry_skin_product_have_stock_df = dry_skin_product_df[dry_skin_product_df.quantity > 0]
                dry_product_have_stock = dict(zip(dry_skin_product_have_stock_df['product'], dry_skin_product_have_stock_df.quantity))

                have_stock_product_list = []
                for i in range(len(dry_product_have_stock)):
                    have_stock_product = f"{list(dry_product_have_stock.keys())[i]} 現時仍有存貨 {list(dry_product_have_stock.values())[i]} 件"
                    have_stock_product_list.append(have_stock_product)
                have_stock_product = ", ".join(have_stock_product_list)

                # Products without stock
                dry_skin_product_no_stock_df = dry_skin_product_df[dry_skin_product_df.quantity == 0]
                no_stock_product_list = list(dry_skin_product_no_stock_df['product'])
                no_stock_product = ", ".join(no_stock_product_list)
                no_stock_product = no_stock_product + " 仍未有存貨"

                message = f'{have_stock_product}\n\n{no_stock_product}'

                dispatcher.utter_message(text=message)

        return []        


class ChangeSkinTypeAction(Action):
    def name(self) -> Text:
        return "action_change_skin_type"

    def run(
        self, 
        dispatcher, 
        tracker: Tracker, 
        domain: "DomainDict"
    ) -> List[Dict[Text, Any]]:

        if tracker.get_intent_of_latest_message() == 'inform_change_skin_type':
            skin_type = tracker.get_slot("change_skin_type")

        return [SlotSet("first_skin_type",skin_type)]

class RestProductorTreatmentAction(Action):
    def name(self) -> Text:
        return "action_reset_product_or_treatment"

    def run(
        self, 
        dispatcher, 
        tracker: Tracker, 
        domain: "DomainDict"
    ) -> List[Dict[Text, Any]]:

        return [SlotSet("product_or_treatment", None)]