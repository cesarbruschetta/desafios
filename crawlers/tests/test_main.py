import unittest
from unittest.mock import patch, MagicMock, PropertyMock

from threads_reddit.main import (
    main_parser,
    main
)


class TestMain(unittest.TestCase):
    @patch("threads_reddit.main.main_parser")
    def test_main(self, mk_process):

        mk_process.return_value = 0
        self.assertRaises(SystemExit, main)
        mk_process.assert_called_once_with(["test"])


class TestMainParser(unittest.TestCase):
    
    def test_main_parser_error(self):
        self.assertRaises(SystemExit, main_parser, ["error"])

    @patch("threads_reddit.main.RedditThreads")
    def test_main_parser_bombando_call_RedditThreads(self, mk_RedditThreads):

        main_parser(["bombando", "test"])
        mk_RedditThreads.assert_called_once_with(["test"])
        
    @patch("threads_reddit.main.print_result_threads")
    @patch("threads_reddit.main.RedditThreads")
    def test_main_parser_bombando_call_print_result_threads(self, mk_RedditThreads, mk_print_result_threads):

        result_mk = MagicMock()
        type(result_mk).results = PropertyMock(return_value={
            "test": [
                {"score": 5000,
                "subreddit":"test", 
                "title": "Teste", 
                "link_comment": "/r/test/comments/xxxxx", 
                "link_thread": "/r/test/"
                }
            ]
        })
        mk_RedditThreads.return_value = result_mk
        main_parser(["bombando", "test"])
        mk_print_result_threads.assert_called_once_with(
             [
                {"score": 5000,
                "subreddit":"test", 
                "title": "Teste", 
                "link_comment": "/r/test/comments/xxxxx", 
                "link_thread": "/r/test/"
                }
            ]
        )
    
    @patch("threads_reddit.main.TelegranBot")
    def test_main_parser_telegram_call_TelegranBot(self, mk_TelegranBot):

        main_parser(["telegram", "--token", "xxxxxx"])
        mk_TelegranBot.assert_called_once_with("xxxxxx")
        