import poplib
# 解析邮件
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


# 解析消息头中的字符串
# 没有这个函数，print出来的会使乱码的头部信息。如'=?gb18030?B?yrXWpL3hufsueGxz?='这种
# 通过decode，将其变为中文
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


# 解码邮件信息分为两个步骤，第一个是取出头部信息
# 首先取头部信息
# 主要取出['From','To','Subject']
'''
From: "=?gb18030?B?anVzdHpjYw==?=" <justonezcc@sina.com>
To: "=?gb18030?B?ztLX1Ly6tcTTys/k?=" <392361639@qq.com>
Subject: =?gb18030?B?dGV4dMTjusM=?=
'''


# 如上述样式，均需要解码
def get_header(msg):
    for header in ['From', 'To', 'Subject']:
        value = msg.get(header, '')
        if value:
            # 文章的标题有专门的处理方法
            if header == 'Subject':
                value = decode_str(value)
            elif header in ['From', 'To']:
                # 地址也有专门的处理方法
                hdr, addr = parseaddr(value)
                name = decode_str(addr)
                # value = name + ' < ' + addr + ' > '
                value = name
        print(header + ':' + value)


# 头部信息已取出


# 获取邮件的字符编码，首先在message中寻找编码，如果没有，就在header的Content-Type中寻找
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


# 邮件正文部分
# 取附件
# 邮件的正文部分在生成器中，msg.walk()
# 如果存在附件，则可以通过.get_filename()的方式获取文件名称

def get_file(msg):
    for part in msg.walk():
        filename = part.get_filename()
        if filename != None:  # 如果存在附件
            filename = decode_str(filename)  # 获取的文件是乱码名称，通过一开始定义的函数解码
            data = part.get_payload(decode=True)  # 取出文件正文内容
            # 此处可以自己定义文件保存位置
            path = filename
            f = open(path, 'wb')
            f.write(data)
            f.close()
            print(filename, 'download')


def get_content(msg):
    for part in msg.walk():
        content_type = part.get_content_type()
        charset = guess_charset(part)
        # 如果有附件，则直接跳过
        if part.get_filename() != None:
            continue
        email_content_type = ''
        content = ''
        if content_type == 'text/plain':
            email_content_type = 'text'
        elif content_type == 'text/html':
            print('html 格式 跳过')
            continue  # 不要html格式的邮件
            email_content_type = 'html'
        if charset:
            try:
                content = part.get_payload(decode=True).decode(charset)
            except AttributeError:
                print('type error')
            except LookupError:
                print("unknown encoding: utf-8")
        if email_content_type == '':
            continue
            # 如果内容为空，也跳过
        print(email_content_type + ' -----  ' + content)


# get_file(msg)
if __name__ == '__main__':

    email = '392361639@qq.com'
    password = 'ngq*******rznbici'

    server = poplib.POP3_SSL('pop.qq.com')
    server.user(email)
    server.pass_(password)
    # 登录的过程
    resp, mails, octets = server.list()
    index = len(mails)  # 邮件的总数
    # 此处的循环是取最近的几封邮件
    for i in range(index - 2, index + 1):
        resp, lines, octets = server.retr(i)  # 取邮件
        msg_content = b'\r\n'.join(lines).decode('utf-8', 'ignore')
        msg = Parser().parsestr(msg_content)
        # server.dele(index) 删除邮件
        get_header(msg)
        get_file(msg)
        get_content(msg)
    server.quit()




    # 下面是发送正文及附件，相对读取邮件信息，发送邮件要比读取要简单很多
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import os

    sender = 'justonezcc@sina.com'
    receiver = '392361639@qq.com'
    subject = 'python email test'
    smtpserver = 'smtp.sina.com'
    password = '***'
    from email import encoders

    msgRoot = MIMEMultipart('alternative')

    msgRoot['Subject'] = subject
    msgRoot['From'] = sender
    msgRoot['To'] = receiver

    # 发送正文
    content = '你好，这是一封测试邮件'
    cont = MIMEText(content, 'plain', 'utf-8')
    msgRoot.attach(cont)

    # 发送附件
    file_name = '实证结果.xls'  # 要发送文件的文字

    row_path = os.getcwd()  # 或者其他路径
    path = os.path.join(row_path, file_name)

    att = MIMEText(open(path, 'rb').read(), 'base64', 'gb2312')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', file_name))
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()