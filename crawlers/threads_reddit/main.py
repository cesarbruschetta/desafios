""" """
import sys
import argparse
import pkg_resources

from threads_reddit.threads_bombando import RedditThreads
from threads_reddit.telegram_bot import TelegranBot
from threads_reddit.utils import print_result_threads


def main_parser(sargs):
    def threads_list(string):
        return string.split(";")

    parser = argparse.ArgumentParser(
        epilog="""Para mais informações de subcomando utilizar o \
            argumento `-h`, exemplo: treadsreddit bombando -h""",
        description="",
    )

    packtools_version = pkg_resources.get_distribution("crawler-treadsreddit").version
    parser.add_argument("--version", action="version", version=packtools_version)

    subparsers = parser.add_subparsers(title="Commands", metavar="", dest="command")

    # THREADS BOMBANDO
    bombando_parser = subparsers.add_parser(
        "bombando",
        help="Gerar e imprimir uma lista contendo a pontuação, subreddit, título da thread, \
            link para os comentários da thread e link da thread.",
    )

    bombando_parser.add_argument(
        "threads",
        type=threads_list,
        help='Lista com nomes de subreddits separados por ponto-e-vírgula (`;`). Ex: "askreddit;worldnews;cats"',
    )

    # THREADS Telegram
    telegram_parser = subparsers.add_parser(
        "telegram",
        help="Inicia o serviço do Bot do Telegram",
    )
    telegram_parser.add_argument("--token", help="Token do Bot do Telegram, fornecido pelo BotFather do Telegram")


    ################################################################################################
    args = parser.parse_args(sargs)

    if args.command == "bombando":

        rt = RedditThreads(args.threads)
        result_threads = rt.results
        SPACE = 20

        print(
            "\n",
            "#" * SPACE,
            "Threads que estão bombando no Reddit naquele momento!",
            "#" * SPACE,
        )
        for thread, result in result_threads.items():
            print("#" * SPACE,thread.title(), "#" * SPACE,)
            print_result_threads(result)

    elif args.command == "telegram":
        
        bot = TelegranBot(args.token)
        bot.register()

    else:
        raise SystemExit(
            "Vc deve escolher algum parametro, ou '--help' ou '-h' para ajuda"
        )

    return 0


def main():
    sys.exit(main_parser(sys.argv[1:]))


if __name__ == "__main__":
    sys.exit(main_parser(sys.argv[1:]))
