#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

if __name__ == "__main__":
    rules = []
    no_rules = []
    with open("text.txt", "r", encoding="UTF-8") as fin:
        for line in fin:
            words = line.lower()
            if re.findall(r'\w*ie\w*', words) or re.findall(r'\w*ei\w*', words):
                if re.findall(r'\w*[^c]ie\w*', words) or re.findall(r'\w*cei\w*', words):
                    ie_words = re.findall(r'\w*[^c]ie\w*', words)
                    ei_words = re.findall(r'\w*cei\w*', words)
                    rules += ie_words + ei_words
                else:
                    no_ie_words = re.findall(r'\w*cie\w*', words)
                    no_ei_words = re.findall(r'\w*[^c]ei\w*', words)
                    no_rules += no_ei_words + no_ie_words

    rules = list(set(rules))
    no_rules = list(set(no_rules))
    print(f"Количество слов, отвечающих правилу: {len(rules)}")
    print(f"Слова, отвечающие правилу: {rules}")
    print(f"Количество слов, не отвечающих правилу: {len(no_rules)}")
    print(f"Слова, не отвечающие правилу: {no_rules}")
