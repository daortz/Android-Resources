# Android commands cheat sheet

## ADB commands

### APK installation

Download the target APK
- APKpure
- EVOZI

#### Instalar desde la PC
```
adb install com.app.name.apk
```

#### Copy from cellphone (USB mode debug)
```
adb shell pm list packages
adb pull /data/app/com.app.name/base.apk /path/destination/folder
```


#### Basic 
```
ADB devices
ADB disconnect <IP>
ADB connect <IP>
ADB shell  <COMANDO>
ADB forward tcp:31415 tcp:31415
adb shell ip address show wlan0
adb shell netstat
adb shell dumpsys
adb shell dumpsys activity
adb shell dumpsys battery
adb shell input text
```

#### Dump
```
ADB MEMORY DUMP COMMANDS
ADB shell ps | grep <APK>
ADB shell am dumpheap <PID> <RUTA>/<FILENAME>
ADB pull <RUTA>/<FILENAME>
Hprof-conv <in-f> <out-f> 
Jhat -port 7000 <out-f>
```

#### LOGCAT
```
ADB logcat -f <output-file>
ADB logcat “:E*” Filtra todos los eventos de tipo error
ADB logcat |  grep -i “foo” Obtiene todo lo que contenga la palabra foo
ADB logcat --pid=<PID> Obtiene los unicamente de la app con PID
```

## SQLite commands
```
SQLITE> .tables
SQLITE> .quit
SQLITE> .help
SQLITE> .schema
SQLITE> CREATE TABLE FOO(name VARCHAR(128)  PRIMARY KEY, value VARCHAR(255) NOT NULL);
SQLITE> CREATE TABLE IF NOT EXIST FOO(name VARCHAR(128) PRIMARY key, value VARCHAR(255) NOT NULL);
SQLITE> SELECT * FROM TABLE_NAME;
SQLITE> SELECT * FROM CLIENTS LIMIT 3
SQLITE> DROP TABLE TABLE_NAME
SQLITE> ALTER TABLE FOO rename to FOOBAR
SQLITE> INSERT INTO FOO (name,value,address) values(‘foo’,’foo1’,’foo2’);
```

