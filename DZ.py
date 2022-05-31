
# -----------------------------------------------------------------------
def dz1(message, bot, chat_id):
    age = message.chat.id
    bot.send_message(chat_id, f"Не молодею уже", age,"лет")

# -----------------------------------------------------------------------
def dz2(bot, chat_id):
    bot.send_message(chat_id, f"нет задания")
# -----------------------------------------------------------------------
def dz3(bot, chat_id):
    bot.send_message(chat_id, f"нет задания")
# -----------------------------------------------------------------------
def dz4(bot, chat_id):
    bot.send_message(chat_id, f"нет задания")

def dz4_ResponseHandler(bot, chat_id, age_int):
    bot.send_message(chat_id, f"нет задания")
# -----------------------------------------------------------------------
def dz5(bot, chat_id):
    bot.send_message(chat_id, f"нет задания")
# -----------------------------------------------------------------------
def dz6(bot, chat_id):
    bot.send_message(chat_id, f"нет задания")
# -----------------------------------------------------------------------
def dz7(bot, chat_id):
    bot.send_message(chat_id, f"нет задания")
# -----------------------------------------------------------------------
def my_input(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, ResponseHandler)
# -----------------------------------------------------------------------
def my_inputInt(bot, chat_id, txt, ResponseHandler):

    # bot.send_message(chat_id, text=botGames.GameRPS_Multiplayer.name, reply_markup=types.ReplyKeyboardRemove())

    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, my_inputInt_SecondPart, botQuestion=bot, txtQuestion=txt, ResponseHandler=ResponseHandler)
    # bot.register_next_step_handler(message, my_inputInt_return, bot, txt, ResponseHandler)  # то-же самое, но короче

def my_inputInt_SecondPart(message, botQuestion, txtQuestion, ResponseHandler):
    chat_id = message.chat.id
    try:
        if message.content_type != "text":
            raise ValueError
        var_int = int(message.text)
        # данные корректно преобразовались в int, можно вызвать обработчик ответа, и передать туда наше число
        ResponseHandler(botQuestion, chat_id, var_int)
    except ValueError:
        botQuestion.send_message(chat_id,
                         text="Можно вводить ТОЛЬКО целое число в десятичной системе исчисления (символами от 0 до 9)!\nПопробуйте еще раз...")
        my_inputInt(botQuestion, chat_id, txtQuestion, ResponseHandler)
# -----------------------------------------------------------------------
