from grammar.checker import Checker
from language.sentence import Sentence


class Buffer:
    STOP_TOKENS = ('.', '\n')

    def __init__(self, max_checker_iterations=10, verbose_checker=False):
        self._buffer = ''
        self._checker = Checker()
        self._max_checker_iterations = max_checker_iterations
        self._verbose_checker = verbose_checker

    # Second return value is the number of processed chars (they won't be processed by the buffer any more)
    # it is useful when the buffer processes only a part of it
    def write_char(self, char: str):
        if char in Buffer.STOP_TOKENS and len(self._buffer) == 0:
            self._buffer = ''
            return char, 1
        if char in Buffer.STOP_TOKENS:
            processed_sent = self._checker.check(Sentence(self._buffer), self._verbose_checker,
                                                 self._max_checker_iterations)
            self._buffer = ''  # Reset buffer
            processed_str = processed_sent.get_striped() + char
            return processed_str, len(processed_str)
        else:
            self._buffer += char
            return self._buffer, 0

    def pop_char(self):
        self._buffer = self._buffer[:-1]

    def set_without_processing(self, text):
        self._buffer = text
        return self._buffer
