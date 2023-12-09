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
        await checkAccess()
        await loadMainScript()
        await LoaderScript()
    });

    const formData = ref({
        title: "",
        description: "",
        datetime: "",
        entry_content: "",
        img_detail: "",
        img: ""
    });

    const error = ref('');

    const createFruit = async () => {
        if (formData.value.title &&
            formData.value.description &&
            formData.value.datetime &&
            formData.value.img_detail &&
            formData.value.img) {
               
                try {
                    const response = await axios.post('http://127.0.0.1:8000/admin/fruits/create', formData.value);
                    console.log('create successful', response.data);
                    router.push('/admin');
                } catch (err) {
                    console.error('create error', err);
                    error.value = err.response.data.detail || 'An error occurred during creation.';
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


    const checkAccess = async () => {
        try {
            setToken()
            const response = await axios.get('http://127.0.0.1:8000/admin/access')
            console.log(response.data)
            if (response.data.access != 1){
                router.push('/');
            }
        }
        catch (err) {
            console.error('error', err);
            router.push('/');
        }
    }


    const setToken = () => {
        const token = localStorage.getItem('token');
        if (token) {
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        } else {
            delete axios.defaults.headers.common['Authorization'];
        }
    }

</script>


<template>
        <Navbar></Navbar>
 
        <section class="ftco-section contact-section bg-light">
      <div class="container">
        <div v-if="error" class="red">{{ error }}</div>
        <div class="row block-9">
          <div class="col-md-6 order-md-last d-flex">
            <form @submit.prevent="createFruit" class="bg-white p-5 contact-form">
              <div class="form-group">
                <input type="text" class="form-control" placeholder="عنوان" v-model="formData.title">
              </div>
              <div class="form-group">
                <input type="text" class="form-control" placeholder="توضیحات" v-model="formData.description">
              </div>
              <div class="form-group">
                <input type="text" class="form-control" placeholder="عکس" v-model="formData.img">
              </div>
              <div class="form-group">
                <input type="text" class="form-control" placeholder="عکس صفحه جزئیات" v-model="formData.img_detail">
              </div>
              <div class="form-group">
                <input type="text" class="form-control" placeholder="تاریخ" v-model="formData.datetime">
              </div>
              <div class="form-group">
                <textarea v-model="formData.entry_content" cols="30" rows="7" class="form-control" placeholder="متن (html)"></textarea>
              </div>
              <div class="form-group">
                <input type="submit" value="ایجاد" class="btn btn-primary py-3 px-5">
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

