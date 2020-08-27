import java.util.Base64;
import java.security.MessageDigest;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;


public class Brute {
    public static void main(String args[]) {
        for(int i=0; i <9999; i++){
            String value = String.valueOf(i);
            String pass = "<=== P3nt3st3rL4b ===>";
            String result = decrypt("G38zckAufW4B9A6sywz28kzgW8CCx1UWugLUTjKlo/kwV1CVesmr0tPX/JZOW0aik0TlkrcAIZZ/G0BigUtmeg==", value, pass);
            if(result != ""){
              printResult(result, String.valueOf(i));

            } 
        }
        
    }

    public static void printResult(String str, String str2){
      System.out.println("Key: " + str);
      System.out.println("Value: " + str2);

    }
    
    public static String decrypt(String str, String str2, String str3) {
        try {
            byte[] decode = Base64.getDecoder().decode(str);
            byte[] bArr = new byte[decode.length];
            byte[] bArr2 = new byte[16];
            System.arraycopy(decode, 0, bArr2, 0, bArr2.length);
            IvParameterSpec ivParameterSpec = new IvParameterSpec(bArr2);
            int length = decode.length - 16;
            byte[] bArr3 = new byte[length];
            System.arraycopy(decode, 16, bArr3, 0, length);
            MessageDigest instance = MessageDigest.getInstance("MD5");
            instance.update(str3.getBytes("UTF-8"));
            instance.update(str2.getBytes("UTF-8"));
            byte[] bArr4 = new byte[16];
            System.arraycopy(instance.digest(), 0, bArr4, 0, bArr4.length);
            SecretKeySpec secretKeySpec = new SecretKeySpec(bArr4, "AES");
            Cipher instance2 = Cipher.getInstance("AES/CBC/PKCS5Padding");
            instance2.init(2, secretKeySpec, ivParameterSpec);
            return new String(instance2.doFinal(bArr3));
        } catch (Exception unused) {
            return "";
        }
    }
}
