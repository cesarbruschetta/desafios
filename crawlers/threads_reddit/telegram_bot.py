""" """

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from threads_reddit.threads_bombando import RedditThreads


class TelegranBot:
    
    def __init__(self, token):
       
        self.updater = Updater(token, use_context=True)
        self.dp = self.updater.dispatcher


    def error(self, update, context):
        print('Update "%s" caused error "%s"' % (update, context.error))


    def message(self, update, context):
        
        thread = []
        for arg in context.args:
            thread += arg.split(";")

        rt = RedditThreads(thread)
        result_threads = rt.results

        for thread, result in result_threads.items():
            update.message.reply_text("Resultados de {0} Bombando".format(thread.title()))    
            update.message.reply_text(" \n".join([
                r["link_comment"] for r in result
                ]) or "Nada para mostar"
            )
        
    
    def register(self):
    
        self.dp.add_handler(CommandHandler("NadaPraFazer", self.message, pass_args=True))
        
        # log all errors
        self.dp.add_error_handler(self.error)
    
        # Start the Bot
        self.updater.start_polling()
    
        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        self.updater.idle()
