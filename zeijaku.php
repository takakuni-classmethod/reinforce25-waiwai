function nonCompliant(){
    // Noncompliant: Does not ensures the request is being sent to the expected destination
    $file = file_get_contents($_POST['r']);
}
