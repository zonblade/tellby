<?php
$mysqli = new mysqli("localhost", "tellby_user", "???", "tellby_db");/** remove secret key */
define("ROOT" , __DIR__ );
define("SQLI" , $mysqli );