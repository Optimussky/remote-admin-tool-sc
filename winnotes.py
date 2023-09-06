import time
from winotify import Notification, audio

toast = Notification(app_id="DDS CDMX Messages",
					 title="Filemon Systems",
					 msg="Pachin Messages, Reporte Diario",
					 icon=r"C:\www\Pruebas\python\networks\remote-admin-too-sc\images\message.png",
					 duration="long")

#toast.set_audio(audio.LoopingAlarm, loop=False)
toast.add_actions(label="Clic aquí", launch="http://fatiga.ssc.cdmx.gob.mx/pid/reporteFatigaXdia.php")
toast.show()