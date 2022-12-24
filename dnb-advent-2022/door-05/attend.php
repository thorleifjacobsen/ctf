<?php
ini_set('display_errors', 'On');
error_reporting(E_ALL);
if(isset($_POST["submit"])){
    try{
    $fname = uniqid($_POST["submit"]);
    $file = fopen("./incoming/".$fname.$_POST["age"], "w");
    $txt = $_POST["name"]." ".$_POST["age"].$_POST["attend"]."\n";
    fwrite($file, $txt);
    echo("Wrote file ".$fname);

    } catch(Exception $e){
        echo $e;
        echo "<br/>";
    }
    fclose($file);
}
?>