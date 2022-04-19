from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() #사용자 model은 장고에서 만들어줌

#미션2 - basic
class Faq(models.Model):
    GENERAL = 'GEN'
    ACCOUNT = 'ACC'
    ETC = 'ETC'
    CATEGORYS = [
        (GENERAL, '일반'),
        (ACCOUNT, '계정'),
        (ETC, '기타'),
    ]
    #1
    question = models.TextField(verbose_name='질문')
    #2
    category = models.CharField(
        verbose_name='카테고리',
        max_length=3,
        choices=CATEGORYS,
        default=GENERAL,
    )
    #3
    answer = models.TextField(verbose_name='답변')
    #4
    writer = models.ForeignKey(verbose_name='생성자', to=User, on_delete=models.CASCADE, null=True, blank=True)
    #5
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    #6
    final_writer = models.ForeignKey(verbose_name='최종 수정자',to=User, on_delete=models.CASCADE, null=True, blank=True, related_name='supportss_Faqs_related') #https://stackoverflow.com/questions/22538563/django-reverse-accessors-for-foreign-keys-clashing reverse accessor for 에러 참고
    #7
    final_created_at = models.DateTimeField(verbose_name='최종 수정일시', auto_now=True)


#미션2 - Advanced
class Inquiry(models.Model):
    '''
    -카테고리 category
    -제목 title
    -이메일 email
    -이메일수신여부 email_rcv_yn
    -문자메세지(핸드폰번호) phone
    -문자수신여부 phone_rcv_yn
    -질문내용 question
    -이미지 image
    -생성자 writer
    -생성일시 created_at
    '''
    GENERAL = 'GEN'
    ACCOUNT = 'ACC'
    ETC = 'ETC'
    CATEGORYS = [
        (GENERAL, '일반'),
        (ACCOUNT, '계정'),
        (ETC, '기타'),
    ]
    #1
    category = models.CharField(
        verbose_name='카테고리',
        max_length=3,
        choices=CATEGORYS,
        default=GENERAL,
    )
    #2
    title = models.TextField(verbose_name='제목')
    #3
    email = models.TextField(verbose_name='이메일')
    #4
    email_rcv_yn = models.BooleanField(verbose_name='이메일수신여부')
    #5
    phone = models.TextField(verbose_name='핸드폰번호')
    #6
    phone_rcv_yn = models.BooleanField(verbose_name='문자수신여부')
    #7
    question = models.TextField(verbose_name='질문내용')
    #8
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    #9
    writer = models.ForeignKey(verbose_name='생성자', to=User, on_delete=models.CASCADE, null=True, blank=True)
    #10
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)


#미션2 - Advanced
class Answer(models.Model):
    '''
    -답변내용 answer
    -참조문의글 ref_inquiry
    -생성자 writer
    -생성일시 created_at -> auto_now_add 사용
    -최종 수정자 final_writer
    -최종 수정일시 final_created_at -> auto_now 사용
    '''
    #1
    answer = models.TextField(verbose_name='답변내용')
    #2
    ref_inquiry = models.ForeignKey(verbose_name='참조문의글', to=Inquiry, on_delete=models.CASCADE)
    #3
    writer = models.ForeignKey(verbose_name='생성자', to=User, on_delete=models.CASCADE, null=True, blank=True)
    #4
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    #5
    final_writer = models.ForeignKey(verbose_name='최종 수정자',to=User, on_delete=models.CASCADE, null=True, blank=True, related_name='supportss_Answers_related')
    #6
    final_created_at = models.DateTimeField(verbose_name='최종 수정일시', auto_now=True)