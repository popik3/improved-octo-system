import logging
from threading import Thread
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from transformers import AutoTokenizer
from ctransformers import AutoModelForCausalLM
from huggingface_hub import hf_hub_download

# 1. Настройки
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

TG_TOKEN = "8155495145:AAF57Zb9lHbEk1jAedqbDz4CrEypabCbmPA"
MODEL_NAME = "deepseek-ai/deepseek-coder-6.7b-instruct"
MODEL_FILE = "deepseek-coder-6.7b-Q4_K_M.gguf"

# 2. Загрузка модели
model = None

def load_model():
    global model
    try:
        model_path = hf_hub_download(
            repo_id=MODEL_NAME,
            filename=MODEL_FILE,
            cache_dir="C:/models"
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            model_type="llama",
            gpu_layers=30,
            threads=6
        )
        logger.info("Модель успешно загружена!")
    except Exception as e:
        logger.error(f"Ошибка загрузки: {e}")

# Запускаем загрузку в фоне
Thread(target=load_model).start()

# 3. Обработчик сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if model is None:
        await update.message.reply_text("⏳ Модель загружается... Попробуйте через 2-3 минуты")
        return
    
    try:
        response = model(update.message.text)
        await update.message.reply_text(f"💡 Ответ:\n{response}")
    except Exception as e:
        await update.message.reply_text(f"❌ Ошибка: {str(e)}")

# 4. Запуск бота
def main():
    app = Application.builder().token(TG_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    logger.info("Бот запущен! Ожидайте загрузки модели...")
    main()