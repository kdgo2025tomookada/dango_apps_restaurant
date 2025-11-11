from django.db import models
from django.urls import reverse

# Create your models here.
#<category>
#カテゴリモデル:飲食店のカテゴリ（例：フレンチ、イタリアン、寿司など）を表現。
class Category(models.Model):
    name = models.CharField(max_length=255)#カテゴリの名前を書くのする文字フィールド（例：フレンチ）
    author = models.ForeignKey(#　カテゴリを作成したユーザーのリレーションシップを表現
        'auth.User',  # Djangoのデフォルトのユーザーモデルを指定
        on_delete=models.CASCADE,  # ユーザーが削除された場合、関連するカテゴリも削除
    )
    created_at = models.DateTimeField(auto_now_add=True)#カテゴリの作成日時を格納する日時フィールド。（自動追加）
    updated_at = models.DateTimeField(auto_now=True)#カテゴリの更新日時を格納する日時フィールド。（自動更新）
    def __str__(self):
        return self.name# カテゴリの名前を文字列として返す。（管理者画面などで表示される）
    
#<shop>
#店舗モデル:飲食店の情報を表現
class Shop(models.Model):
    name = models.CharField(max_length=255)# 飲食店の名前を格納する文字列フィールド
    address = models.CharField(max_length=255)# 飲食店の住所を書くの巣うる文字列フィールド
    author = models.ForeignKey(# 飲食店を作成したユーザーとのリレーションシップを表現
        'auth.User',  # Djangoのデフォルトのユーザーモデルを指定
        on_delete=models.CASCADE,# ユーザーが削除された場合、関連する店舗も削除。
    )
    category = models.ForeignKey(# 飲食店のカテゴリとのリレーションシップを表現
        Category,# カテゴリモデルとのリレーションシップ
        on_delete=models.PROTECT,# 関連するカテゴリが削除されても削除されない。
    )
    created_at = models.DateTimeField(auto_now_add=True)# 飲食店の作成日時を格納する日時フィールド（自動追加）
    updated_at = models.DateTimeField(auto_now=True)# 飲食店の更新日時を格納する日時フィールド（自動更新）
    def __str__(self):
        return self.name# 飲食店の名前を文字列として返す（管理画面などで表示される。）
    
    def get_absolute_url(self):
        return reverse('gourmet_guide:detail', kwargs={'pk': self.pk})