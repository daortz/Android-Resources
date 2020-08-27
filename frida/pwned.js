/* 
   Author: 0xD0tz
   Date: 14/05/19
*/


const ENIGMA_LIB = "pwned-lib.so";

// Main

Java.perform(function () {
    
    // Set upaId 

    var clientInfo = Java.use('com.pwned.classHook').$new();
    clientInfo.setUpaId.implementation =  function(str){
        return this.setUpaId(str);
    }
    
    // Get token

   
    for(var i =0; i < 1000; i++){
        var fakeUpa = Math.random().toString(36).substring(2,20) + Math.random().toString(36).substring(2,20);
        var fakeContext = Math.random().toString(36).substring(2,20) + Math.random().toString(36).substring(2,20);
        clientInfo.setUpaId(fakeUpa);
        var upa = clientInfo.getUpaId();
        console.log(getValidToken(fakeContext,upa, full));

    }
    
   

    // ================================ Activity Hooking ================================= //


    // HomeActivity
    var HomeActivity = Java.use('com.pwned.HomeActivity');
    HomeActivity.innerOnCreate.implementation = function(bundle){
        return this.bundle;
    };

    // LoginFlow Activity
    var LoginFlowActivity = Java.use('com.pwned.LoginFlowActivity');
    LoginFlowActivity.onCreate.implementation  = function(bundle){
        send("GO")
        return this.onCreate(bundle)
       
    };

    // =================================== Functions ================================= //

    function getValidToken(fakeContext, upa, url){
        var t = Java.use('ar.com.pwned.account.Sec').$new();
        t.token.overload('java.lang.String', 'java.lang.String', 'java.lang.String').implementation = function(x, y, z) {
            return this.token(x,y,z);
    
        }
        return t.token(fakeContext, upa.toString(), url);
    }

    function enigmaInspection(moduleName){
        var enigmaModuleName = moduleName;
        Module.enumerateSymbolsSync(enigmaModuleName).forEach(function(symbol){
            switch(symbol.name){
                case "_EnigmaModuleNameSymbols":
                    var RegisterNativeMethodPtr = symbol.path;
                    Interceptor.Attach(RegisterNativeMethodPtr, {
                        onEnter: function(args){

                        },
                        onLeave: function(args){

                        }
                    });
                    break;
                case "_ZntineinlibraEnigma":
                Interceptor.Attach(symbol.address, {
                    onEnter: function(args){
                        if(args[1] != null){
                            jclassAddress2NameMap[args[0]] =  Memory.readCString(args[1]);
                        }
                    },
                    onLeave: function(args){}
                })
            }
        });
    }
    
    
    function inspectModule(name){
        var libc = Module.findBaseAddress(name);
        console.log(hexdump(libc,{
            offset: 0,
            length: 1024,
            header: true,
            ansi: true
        }));
    }


    function getContext(){
        var context = Java.use('android.app.ActivityThread').currentApplication().getApplicationContext().getContentResolver();
        return context;
    }

    function getIMEI(){
        console.log('IMEI: ', Java.use('android.telephony.TelephonyManager').$new().getDeviceId());
    }

    function getProcessInfo(){
        send("============= Process Description =============[*]")
        send("Process ID: " + Process.id);
        send("Process arch: " + Process.arch);
    }
    
    function enumModules(){
        
        var modules = Process.enumerateModules().forEach(function(module){
            send("Module: " + module.name);
            send("Module base: " + module.base);
            
        })
        
    }

    function infoModule(name){
        var module = Module.load(name);
        console.log(module.name);
        console.log(module.base);
        console.log(module.size);
        console.log(module.path);

    }
 
});