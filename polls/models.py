from django.db import models
import datetime # Pythonの標準モジュール
from django.utils import timezone # タイムゾーン関連のユーティリティ

class Question(models.Model):

    # 問題を書くテキストのフィールドを作成
    question_text = models.CharField(max_length=200) # CharFieldには、max_lengthを指定する必要がある　

    # パブリッシュの日付作成
    pub_date = models.DateTimeField('date published')

    # 文字列を定義
    def __str__(self):
        return self.question_text

    # パブリッシュの時間を定義
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):

    # 選択肢を作成
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # 選択肢の文を書くテキストのフィールドを作成
    choice_text = models.CharField(max_length=200)

    # 投票を作成
    votes = models.IntegerField(default=0)

    # 文字列を定義
    def __str__(self):
        return self.choice_text
