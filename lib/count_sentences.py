#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value=''):
    if(type(value) == str):
      self._value = value
    else:
      print('The value must be a string.')

  def is_sentence(self):
    return True if self.value[len(self.value) - 1] == '.' else False

  def is_question(self):
    return True if self.value[len(self.value) - 1] == '?' else False

  def is_exclamation(self):
    return True if self.value[len(self.value) - 1] == '!' else False

  def count_sentences(self):
    no_excalamation = self.value.replace('!','.')
    no_question = no_excalamation.replace('?','.')
    split_sentences = no_question.split('. ')
    if self.value == '' or '.' not in self.value:
      return 0
    else:
      return len(split_sentences)