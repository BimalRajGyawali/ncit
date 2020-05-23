document.getElementById('login').addEventListener('click',()=>{

      event.preventDefault();
      let rollField = document.getElementById('roll');
      let rollFieldError = document.getElementById('roll-error');
      let passwordField = document.getElementById('password');
      let passwordFieldError = document.getElementById('pswd-error');
      let loginBtn = event.target;

      let roll = rollField.value;
      let password = passwordField.value;

      if(isEmpty(roll)){
          displayError(rollField, rollFieldError, 'Roll is a required field');
            rollField.addEventListener('keydown', ()=>{
             reset(rollField, rollFieldError);
          });
          return false;
      }

      if(isInvalid(roll)){
        displayError(rollField, rollFieldError, `${roll} is not a valid roll number`);
          rollField.addEventListener('keydown', ()=>{
             reset(rollField, rollFieldError);
          });
        return false;
      }

      if(isEmpty(password)){
          displayError(passwordField, passwordFieldError, 'Password is a required field');
          passwordField.addEventListener('keydown', ()=>{
             reset(passwordField, passwordFieldError);
          });
          return false;
      }

      if(containsSpaces(password) || isShort(password)){
         displayError(passwordField, passwordFieldError, 'Invalid password format');
         passwordField.addEventListener('keydown', ()=>{
             reset(passwordField, passwordFieldError);
          });
         return false;
      }

      loadGif(loginBtn);
      /* ajax */
      rollField.disabled = true;
      passwordField.disabled = true;

      let studentData = {
            roll: parseInt(document.getElementById('roll').value),
            password : password
      }


      let response = postData('/accounts/login-ajax/', studentData);

      response
      .then(data => {
          if(data.success){
             resetGif(loginBtn, 'Login');
             rollField.disabled = false;
             passwordField.disabled = false;
             window.location.href = '/accounts/student-home/';
          }else{
             resetGif(loginBtn, 'Login');
             rollField.disabled = false;
             passwordField.disabled = false;
             displayError(passwordField, passwordFieldError, data.msg);
             passwordField.style.outline = '';

          }

      })
      .catch(error=>{
             resetGif(loginBtn, 'Login');
             rollField.disabled = false;
             passwordField.disabled = false;
             displayError(passwordField, passwordFieldError, "Something went wrong.");
             passwordField.style.outline = '';


      })


});
