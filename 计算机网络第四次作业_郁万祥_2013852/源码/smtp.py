
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方SMTP服务
mail_host = "smtp.qq.com" # 设置服务器
#自己的邮箱，通过QQ邮箱设置获取口令
mail_user = "2276227539@qq.com" #用户名
mail_pass = "sqbwwgbkbajteacc" #口令
#sqbwwgbkbajteacc
#pumacovuuctydjdi
sender = '2276227539@qq.com'
receivers = ["yuwanxiang0114@163.com"] #接受者的邮箱,我的另一个QQ邮箱
 
'''
如果发送HTML格式的邮件，那么改变MIME类型就可以
发送HTML格式的邮件与发送纯文本消息的邮件不同之处就是将MIMEText中_subtype设置为html
mail_msg = """
<p>Python 邮件发送测试...<p>
<p><a href="http://www.baidu.com">这是一个链接</a></p>
"""
message=MIMEText(mail_msg, 'html', 'utf-8')
'''
 
# class email.mime.text.MIMEText(_text[, _subtype[, _charset]]) 用于创建主要类型文本的MIME对象，_text是有效负载的字符串,_subtype
# 是次要类型，默认为plain._charset是文本的字符集
message  = MIMEText('i love computer networks', 'plain', 'utf-8')
message['From'] = Header("yuwanxiang", 'utf-8')
message['To'] = Header("2276227539@qq.com", 'utf-8')
 
subject = '邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host, 25) # 25为SMTP端口号
	smtpObj.login(mail_user, mail_pass) #会返回(状态码, "字符串解释")元组信息
	smtpObj.sendmail(sender, receivers, message.as_string())
	print("邮件发送成功")
except smtplib.SMTPException:
	print("Error: 无法发送邮件")
 
"""
<smtplib.SMTP object at 0x000001ED3DDFCE48>
邮件发送成功
[Finished in 2.9s] 
大家可以在QQ邮箱上设置中账号菜单设置开启STMP服务，然后获得口令，填入mail_pass,这里我就用xxxx表示口令，可以看到邮件发送成功 
注: sender和mail_user要相同，可能QQSTMP服务器需要知道真实的发送者，所以就这样
"""
