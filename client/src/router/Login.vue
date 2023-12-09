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
    });

    const formData = ref({
        username: '',
        password: '',
    });

    const error = ref('');

    const getCurrentUser = async (token) => {
        if (token) {
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        } else {
            delete axios.defaults.headers.common['Authorization'];
        }
        const response = await axios.get('http://127.0.0.1:8000/current_user');
        return response.data
    } 

    const loginUser = async () => {
        if (formData.value.password &&
            formData.value.username) {
            
            const formDataAuth = new FormData();
            formDataAuth.append('username', formData.value.username);
            formDataAuth.append('password', formData.value.password);

            try {
                const response = await axios.post('http://127.0.0.1:8000/login', formDataAuth);
                localStorage.setItem('token', response.data.access_token);
                const user = await getCurrentUser(response.data.access_token)
                localStorage.setItem('user', JSON.stringify(user));
                router.push('/');
            } catch (err) {
                console.error('Registration error', err);
                error.value = err.response.data.detail || 'An error occurred during registration.';
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
            <form @submit.prevent="loginUser" class="bg-white p-5 contact-form">
              <div class="form-group">
                <input type="text" class="form-control" placeholder="نام کاربری" v-model="formData.username">
              </div>
              <div class="form-group">
                <input type="password" class="form-control" placeholder="کلمه عبور" v-model="formData.password">
              </div>
              <div class="form-group">
                <input type="submit" value="ورود" class="btn btn-primary py-3 px-5">
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

