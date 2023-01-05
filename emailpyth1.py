import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('abhishekkvk98@gmail.com','fznlgfmvuhmsryka')
msg="hello abhishek"
s.sendmail('abhishekkvk98@gmail.com',['abhishekkvk2017@gmail.com','abhishekkvk20@gmail.com'],msg)
print("Mail Send successfully")
s.quit()