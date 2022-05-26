<?php

ob_start(); 

$API_KEY='5301329263:AAEdQCUYdYsh8RcVBweTiuu5BB2JMCCust0;

define('API_KEY',$API_KEY); 

functin bot($method,$datas=[]){

   $url = "https://api.Telegram.org/bot".API_KEY."/".$method; 

   $ch = curl_init(); 

   curl_setopt($ch,CURLOPT_URL,$url); 

   curl_setopt($ch,CURLOPT_RETURNTRANSFER,true); 

   curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);

   $res = curl_exec($ch)); 

   if(curl_error($ch)){

       var_dump(curl_error($ch)); 

   }else{

       return jso_ decode($res); 

   } 

} 

$update = json_decode(file_contents('php://input)); 

$kt = json_decode(file_get_contents('kt.json'),1);

$admin = "00"; #ايدي

if($text == "اضف كت" and $from_id == $admin){

$kt["k"] = "k";

file_put_contents("kt.json",json_encode($kt));

bot('sendmessage',[

'chat_id'=>$chat_id,

'text'=>"• حسنا عزيزي قم بالرسال كلمه كت",

'reply_to_message_id'=>$message->message_id, 

'reply_markup'=>json_encode([

'inline_keyboard'=>[

[['text'=>"الغاء",'callback_data'=>'no_kt']]

]])

]);

}

if($text != "اضف كت" and $kt["k"] == "k" and $from_id == $admin){

unset($kt["k"]);

$kt["kt"][] = $text;

file_put_contents("kt.json",json_encode($kt));

bot('sendmessage',[

'chat_id'=>$chat_id,

'text'=>"تم الحفظ الكلمه $text",

'reply_to_message_id'=>$message->message_id, 

]);

}

if($text == "حذف كت" and $from_id == $admin){

$kt["k"] = "del";

file_put_contents("kt.json",json_encode($kt));

bot('sendmessage',[

'chat_id'=>$chat_id,

'text'=>"• حسنا عزيزي قم بالرسال كلمه كت للحذفها",

'reply_to_message_id'=>$message->message_id, 

'reply_markup'=>json_encode([

'inline_keyboard'=>[

[['text'=>"الغاء",'callback_data'=>'no_kt']]

]])

]);

}

if($text != "حذف كت" and $kt["k"] == "del" and $from_id == $admin){

if(in_array($text,$kt["kt"])){

$setwit = array_search("$text", $kt["kt"]);

unset($kt["k"]);

unset($kt["kt"][$setwit]);

file_put_contents("kt.json",json_encode($kt)); 

bot('sendMessage', [

'chat_id' =>$chat_id,

'parse_mode' => "تخفيض السعر" ،

'text' => "• تم حذف الكلمه $ text"،

'reply_to_message_id' => $ message-> message_id ،

]) ؛

}آخر{

bot ("sendMessage" ، [

'chat_id' => chat_id دولار ،

'parse_mode' => "تخفيض السعر" ،

'text' => "عذرا لا يوجد هاكذا كلمه $ text"،

'reply_to_message_id' => $ message-> message_id ،

]) ؛

}}

إذا ($ data == "no_kt" و $ from_id == $ admin) {

bot ("حذف الرسالة" ، [

'chat_id' => $ chat_id2 ،

'message_id' => $ message_id2 ،

]) ؛

bot ('answerCallbackQuery'، [

'callback_query_id' => تحديث $-> callback_query-> id ،

'message_id' => $ message_id ،

'text' => "• تم الغاء الكت"،

'show_alert' => صحيح

]) ؛

unset ($ kt ["k"])؛

file_put_contents ("kt.json"، json_encode ($ kt)) ؛

}

$ ki = kt $ ["kt"]؛

$ kt1 = array_rand ($ ki، 1) ؛

طقم $ = ki [$ kt1] ؛

if($text == "كت" and $from_id == $admin){

if($kt["kt"] != null){

bot('sendmessage',[

'chat_id'=>$chat_id,

'text'=>"$kit",

'reply_to_message_id'=>$message->message_id, 

]);

}else{

bot('sendmessage',[

'chat_id'=>$chat_id,

'text'=>"• لا يوجد كت تويت",

'reply_to_message_id'=>$message->message_id, 

]);

}}

if($text == "الأسئلة" and $from_id == $admin){

if($kt["kt"] != null){

bot('sendmessage',[

'chat_id'=>$chat_id,

'text'=>"عدد الكت موجوده في البوت :".count($ki),

'reply_to_message_id'=>$message->message_id, 

]);

}else{

bot('sendmessage',[

'chat_id'=>$chat_id,

'text'=>"• لا يوجد كت تويت",

'reply_to_message_id'=>$message->message_id, 

]);

}}

if($text == "مسح الكت" and $from_id == $admin){

bot('sendmessage',[

'chat_id'=>$chat_id,

'text'=>"تم حذف جميع الكت موجوده",

]);

unset($kt["kt"]);

file_put_contents("kt.json",json_encode($kt)); 

}
