<script setup>
    import { ref, onMounted } from 'vue'
    import { LoaderScript, loadMainScript } from '/src/assets/js/main.js'

    import Navbar from '../components/Navbar.vue'
    import Footer from '../components/Footer.vue'
    import Loader from '../components/Loader.vue'

    import axios from 'axios'
    import { useRouter } from 'vue-router';

    const router = useRouter();

    onMounted( async () => {
        await loadMainScript()
        await LoaderScript()
        console.log("loaded")
    });

    const confrimPassword = ref('')

    const formData = ref({
        username: '',
        password: '',
        fullname: '',
        phone: '',
        age: ''
    });

    const error = ref('');

    const registerUser = async () => {
        if (formData.value.password &&
            formData.value.username &&
            formData.value.fullname &&
            formData.value.age &&
            formData.value.phone &&
            confrimPassword.value) {

            if (formData.value.password == confrimPassword.value){
                try {
                    const response = await axios.post('http://127.0.0.1:8000/register', formData.value);
                    console.log('Registration successful', response.data);
                    router.push('/login');
                } catch (err) {
                    console.error('Registration error', err);
                    error.value = err.response.data.detail || 'An error occurred during registration.';
                }
            }
            else{
                window.scrollTo({
                    top: 0,
                    behavior: 'auto'
                });
                error.value = "تکرار کلمه عبور درست وارد نشده است"
            }
        }
        else {
            window.scrollTo({
                top: 0,
                behavior: 'auto'
            });
            error.value = "تمام فیلد ها پر نشده است"
        }
        
    };

</script>


<template>
        <Navbar></Navbar>
 
        <section class="ftco-section contact-section bg-light">
      <div class="container">
        <div v-if="error" class="red">{{ error }}</div>
        <div class="row block-9">
          <div class="col-md-6 order-md-last d-flex">
            <form @submit.prevent="registerUser" class="bg-white p-5 contact-form">
              <div class="form-group">
                <input type="text" class="form-control" placeholder="نام کاربری" v-model="formData.username">
              </div>
              <div class="form-group">
                <input type="text" class="form-control" placeholder="نام و نام خانوادگی" v-model="formData.fullname">
              </div>
              <div class="form-group">
                <input type="text" class="form-control" placeholder="شماره تلفن" v-model="formData.phone">
              </div>
              <div class="form-group">
                <input type="text" class="form-control" placeholder="سن" v-model="formData.age">
              </div>
              <div class="form-group">
                <input type="password" class="form-control" placeholder="کلمه عبور" v-model="formData.password">
              </div>
              <div class="form-group">
                <input type="password" class="form-control" placeholder="تکرار کلمه عبور" v-model="confrimPassword">
              </div>
              <div class="form-group">
                <input type="submit" value="ثبت نام" class="btn btn-primary py-3 px-5">
              </div>
            </form>
          
          </div>

        </div>
      </div>
    </section>

   
        <Footer></Footer>

        <Loader></Loader>

</template>
  
<style>
   .red{
    color: red
   }
</style>

