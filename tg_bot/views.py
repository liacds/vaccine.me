from django.shortcuts import render

# Create your views here.
import json
import os

import requests
from django.http import JsonResponse
from django.views import View
import json
from home.models import MedOrganization
from .models import ChatContext

TELEGRAM_URL = "https://api.telegram.org/bot"
TUTORIAL_BOT_TOKEN = os.environ.get("TUTORIAL_BOT_TOKEN")
update = 'Сообщить об изменении'  #keyboard
change_type_1 = '1 тип'
change_type_2 = '2 тип'
change_both = "1 и 2 типы"
in_stock = 'Есть в наличии'
out_of_stock = 'Нет в наличии'
yes = 'Да'
no = 'Нет, вернуться в начало'


class TutorialBotView(View):
    def post(self, request, *args, **kwargs):
        t_data = json.loads(request.body)
        if "message" in t_data:
            t_message = t_data["message"]
            t_chat = t_message["chat"]
            chat_id = t_chat["id"]
            try:
                text = t_message["text"].strip()
            except Exception as e:
                return JsonResponse({e: "Error occured"})
            organization = MedOrganization.objects.filter(name=text).first()
            if text == '/start':
                text = "Добро пожаловать в бот для Vaccine.me. Здесь вы можете обновить информацию о наличии вакцины"
                markup = [[update]]
                self.send_message(text, chat_id, markup)
            elif text == update:
                ChatContext.objects.create(user=chat_id)
                buttons = self.output_all_clinics()
                self.send_message(text, chat_id, buttons)
            elif organization:
                chat_context = ChatContext.objects.filter(user = chat_id).first()
                if chat_context:
                    chat_context.organization = organization
                    chat_context.save()
                markup = [[change_type_1], [change_type_2], [change_both]]
                text = "Выберите компонент вакцины"
                self.send_message(text, chat_id, markup)
            elif text == change_type_1 or text == change_type_2 or text == change_both:
                chat_context = ChatContext.objects.filter(user=chat_id).first()
                if chat_context:
                    chat_context.type = text
                    chat_context.save()
                text = "Статус наличия"
                markup = [[in_stock], [out_of_stock]]
                self.send_message(text, chat_id, markup)
            elif text == in_stock or text == out_of_stock:
                chat_context = ChatContext.objects.filter(user=chat_id).first()
                if chat_context:
                    chat_context.update = text
                    chat_context.save()
                text = "Хотите ли вы подтвердить свой запрос: клиника " + chat_context.organization.name + ", "  + chat_context.type + ', ' + chat_context.update
                markup = [[yes], [no]]
                self.send_message(text, chat_id, markup)
            elif text == yes:
                chat_context = ChatContext.objects.filter(user=chat_id).first()
                self.handle_change_request(chat_context)
                text = "Спасибо, ваш запрос получен"
                markup = [[update]]
                self.send_message(text, chat_id,markup)
            elif text == no:
                chat_context = ChatContext.objects.filter(user=chat_id).first()
                if chat_context:
                    chat_context.delete()
                markup  = [[update]]
                self.send_message(text, chat_id, markup)

        return JsonResponse({"ok": "POST request processed"})

    @staticmethod
    def send_message(message, chat_id, markup=None):

        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown",
        }
        if markup:
            data["reply_markup"] = json.dumps({
                "keyboard": markup,
                "one_time_keyboard": True,
                "resize_keyboard": True,
            })

        response = requests.post(
            f"{TELEGRAM_URL}{TUTORIAL_BOT_TOKEN}/sendMessage", data=data
        )
        return JsonResponse({"ok": "POST request processed"})

    #inline markup
    def output_all_clinics(self):
        organizations = MedOrganization.objects.all()
        buttons = []
        for organization in organizations:
            button = [organization.name]
            buttons.append(button)
        return buttons

    def handle_change_request(self, chat_context):
        if chat_context:
            organization = chat_context.organization
            type = chat_context.type
            update = chat_context.update
            if type ==change_type_1:
                if update == in_stock:
                    organization.type_1_stock = True
                if update == out_of_stock:
                    organization.type_1_stock = False
            elif type ==change_type_2:
                if update == in_stock:
                    organization.type_2_stock = True
                if update == out_of_stock:
                    organization.type_2_stock = False
            organization.save()
            chat_context.delete()




