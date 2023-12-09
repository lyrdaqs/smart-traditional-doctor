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
        await setUser()
        await loadMainScript()
        await LoaderScript()
    });

    const username = ref('')

    const formData = ref({
        fullname: '',
        phone: '',
        age: ''
    });

    const error = ref('');
    const success = ref('');

    
    const secureRoute = async () => {
        let response = {}
        try {
            const token = localStorage.getItem('token');
            if (token) {
                axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
            } else {
                delete axios.defaults.headers.common['Authorization'];
            }
            response = await axios.get('http://127.0.0.1:8000/current_user')
        }
        catch {
            router.push('/login');
        }
        return response.data
    }
    
    
    const setUser = async () => {
        const user = await secureRoute()
        username.value = user.username
        formData.value.fullname = user.fullname
        formData.value.phone = user.phone
        formData.value.age = user.age
    }

    const setToken = () => {
        const token = localStorage.getItem('token');
        if (token) {
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        } else {
            delete axios.defaults.headers.common['Authorization'];
        }
    } 

    const updateUser = async () => {
        if (formData.value.fullname &&
            formData.value.age &&
            formData.value.phone) {

            try {
                setToken()
                const response = await axios.put('http://127.0.0.1:8000/user/update', formData.value);
                console.log('update successful', response.data);
                localStorage.removeItem('user')
                localStorage.setItem('user', JSON.stringify(response.data));
                success.value = "مشخصات شما با موفقیت ثبت شد"
            } catch (err) {
                console.error('update error', err);
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
        <div v-if="success" class="green">{{ success }}</div>
        <div class="row block-9">
          <div class="col-md-6 order-md-last d-flex">
            <form @submit.prevent="updateUser" class="bg-white p-5 contact-form">
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
                <input type="submit" value="ثبت تغییرات" class="btn btn-primary py-3 px-5">
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
   .green{
    color: green
   }
</style>

