import pdfkit
import wechatsogou,time
class  WkHtmlToPdf:
      '''微信文章url转pdf'''
      @staticmethod
      def wechaturltopdf(url,title,captcha_break_time=3,wkhtmltopdf='../wkhtmltopdf.exe',outputpath=str(int(time.time()))+'.pdf'):
          ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=captcha_break_time)
          content_info = ws_api.get_article_content(url)
          html =f'''
              <!DOCTYPE html>
              <html lang="en">
              <head>
                  <meta charset="UTF-8">
                  <title>{title}</title>
              </head>
              <body>
              <h2 style="text-align: center;font-weight: 400;">{title}</h2>
              {content_info['content_html']}
              </body>
              </html>'''
          config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf)
          pdfkit.from_string(html,outputpath, configuration=config)
      @staticmethod
      def articleutltopdf(url,captcha_break_time=8,wkhtmltopdf='../wkhtmltopdf.exe', outputpath=str(int(time.time()))+'.pdf',options={'enable-local-file-access': None}):
             config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf)
             pdfkit.from_url(url,outputpath,configuration=config,options=options)


