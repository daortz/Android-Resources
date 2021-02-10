
# ADB Commands

### invoke Activity
adb shell am start -n package-name/activity-name -a android.intent.action.VIEW -d "schema://host"

### testing deeplinks
adb shell am start -W -a android.intent.action.VIEW -d "schema://host"  package-name

### invoke activity with extras
adb shell am start -n package-name/activity-name  -es "destinationUrl" "www.google.com" 

adb shell am start -W -a android.intent.action.VIEW -d "schema://host/"  package-name

# Install FRIDA

$ adb root # might be required
$ adb push frida-server /data/local/tmp/
$ adb shell "chmod 755 /data/local/tmp/frida-server"
$ adb shell "/data/local/tmp/frida-server &"


# find dangerous JS functions 

grep -HrnE "eval\(|setTimeout\(|setInterval\(|Function\(|unserialize\(" . --color --exclude-dir=doc --exclude-dir=decorators

grep -HnrE "(\s\.(route|get|post\('\/sales)\('|router\.)" . --color

grep -HrnE "\s(app|route|router)\.(post|get|delete|patch)" . --color

grep -HrnE "req\.(body|.*)" . --color

grep -Hrne "\s.*(assert|assert\.)\(.*\)" . --color  # looks for any variant of assert

# FFUZ 

### Simple wordlist
ffuf -w objects.txt -u https://targetURL/FUZZ -r  -x "http://127.0.0.1:8080"

### Scan with recursion

### Look for specific extension
ffuf -u https://codingo.io/FUZZ -w ./wordlist -recursion -e .bak

### Fuzzing multiple locations
ffuf -u https://W2/W1 -w ./wordlist.txt:W1,./domains.txt:W2


# INTERLACE

## run ffuf over multiple sites
interlace -tL ./urls.txt -threads 5 -c "ffuf -w ./wordlist.txt -u _target_ -recursion -ms 200,204,301,302,307,401"

## run a list of commands againts target host

commands.txt
```
trivy filesystem _target_ > _output_/_target_-trivy.txt
gitleaks --repo-path=_target_ -v --pretty >  _output_/_target_-gitleaks.txt

```

interlace -tL ./targets.txt -o ~/Engagements/example/ -cL ./commands.txt 
