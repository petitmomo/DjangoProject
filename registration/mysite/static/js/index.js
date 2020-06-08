 var form_fields = document.getElementsByTagName("input")
 form_fields[1].placeholder='First Name';
 form_fields[2].placeholder='Nom';
 form_fields[3].placeholder='Number';
 form_fields[4].placeholder='Email';
 form_fields[5].placeholder='Mot de passe';
 form_fields[6].placeholder='Conf mot de passe';


  for (var field in form_fields){
      form_fields[field].className += 'form-control
  }

