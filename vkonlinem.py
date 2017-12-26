import vk
import time
import smtplib
import pyaudio  
import wave  


session = vk.Session()
vk_api = vk.API(session)
status=0
while True:
    a=vk_api.users.get(user_id=265140292, fields='online')
    if status==0:
        if a[0]['online']==1:
            print(a[0]['last_name'],' ',a[0]['first_name'],' is online')
            status=1
            #define stream chunk   
            chunk = 1024  

            #open a wav format music  
            f = wave.open(r"res1.wav","rb")  
            #instantiate PyAudio  
            p = pyaudio.PyAudio()  
            #open stream  
            stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                            channels = f.getnchannels(),  
                            rate = f.getframerate(),  
                            output = True)  
            #read data  
            data = f.readframes(chunk)  

            #play stream  
            while data:  
                stream.write(data)  
                data = f.readframes(chunk)  

            #stop stream  
            stream.stop_stream()  
            stream.close()  

            #close PyAudio  
            p.terminate()  
    else:
        if a[0]['online']==0:
            print(a[0]['last_name'],' ',a[0]['first_name'],' is offline')
            status=0
    time.sleep(20)
