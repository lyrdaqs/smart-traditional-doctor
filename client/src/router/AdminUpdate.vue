<script setup>
    import { ref, onMounted } from 'vue'
    import { LoaderScript, loadMainScript } from '/src/assets/js/main.js'

    import Navbar from '../components/Navbar.vue'
    import Footer from '../components/Footer.vue'
    import Loader from '../components/Loader.vue'

    import axios from 'axios'
    import { useRouter, useRoute } from 'vue-router';

    const router = useRouter();
    const route = useRoute();

    onMounted( async () => {
        await checkAccess()
        await setFruit()
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

    const updateFruit = async () => {
        if (formData.value.title &&
            formData.value.description &&
            formData.value.datetime &&
            formData.value.img_detail &&
            formData.value.img) {
                
                const fruitId = route.params.id;
                try {
                    const response = await axios.put(`http://127.0.0.1:8000/admin/fruits/${fruitId}/update`, formData.value);
                    console.log('update successful', response.data);
                    router.push('/admin');
                } catch (err) {
                    console.error('update error', err);
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

    const fetchFruit = async () => {
        try {
            const fruitId = route.params.id;
            const response = await axios.get(`http://127.0.0.1:8000/fruits/${fruitId}`);
            return response.data
        } catch (error) {
            console.error('Error fetching fruit:', error);
        }
    };

    const setFruit = async () => {
        const fruit = await fetchFruit()
        formData.value.title = fruit.title
        formData.value.description = fruit.description
        formData.value.datetime = fruit.datetime
        formData.value.entry_content = fruit.entry_content
        formData.value.img_detail = fruit.img_detail
        formData.value.img = fruit.img
    }

</script>


<template>
        <Navbar></Navbar>
 
        <section class="ftco-section contact-section bg-light">
      <div class="container">
        <div v-if="error" class="red">{{ error }}</div>
        <div class="row block-9">
          <div class="col-md-6 order-md-last d-flex">
            <form @submit.prevent="updateFruit" class="bg-white p-5 contact-form">
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
                <input type="submit" value="به روز رسانی" class="btn btn-primary py-3 px-5">
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

