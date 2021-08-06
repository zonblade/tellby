<?php

$url = 'https://api.sendgrid.com/';
$user = '???'; /** remove secret key */
$pass = '???'; /** remove secret key */

$json_string = array(

    'to' => array(
        '???', '???' /** remove secret key */
    ),
    'category' => 'test_category'
);


$params = array(
    'api_user'  => $user,
    'api_key'   => $pass,
    'x-smtpapi' => json_encode($json_string),
    'to'        => '???',/** remove secret key */
    'subject'   => 'testing from curl',
    'html'      => 'testing body',
    'text'      => 'testing body',
    'from'      => 'noreply@mail.tell.by',
);


$request =  $url.'api/mail.send.json';

// Generate curl request
$session = curl_init($request);
// Tell curl to use HTTP POST
curl_setopt ($session, CURLOPT_POST, true);
// Tell curl that this is the body of the POST
curl_setopt ($session, CURLOPT_POSTFIELDS, $params);
// Tell curl not to return headers, but do return the response
curl_setopt($session, CURLOPT_HEADER, false);
// Tell PHP not to use SSLv3 (instead opting for TLS)
curl_setopt($session, CURLOPT_SSLVERSION, CURL_SSLVERSION_TLSv1_2);
curl_setopt($session, CURLOPT_RETURNTRANSFER, true);

// obtain response
$response = curl_exec($session);
curl_close($session);

// print everything out
print_r($response);

?>
