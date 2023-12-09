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
        await fetchFruits()
        await loadMainScript()
        await LoaderScript()
    });

    const fruits = ref([]);

    
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


    const fetchFruits = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/fruits');
            fruits.value = response.data;
        } catch (error) {
            console.error('Error fetching posts:', error);
        }
    };


    const setToken = () => {
        const token = localStorage.getItem('token');
        if (token) {
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        } else {
            delete axios.defaults.headers.common['Authorization'];
        }
    } 

    const getHrefUrl = (id) => {
        return `/admin/update/${id}`;
    };

    const deleteFruit = async (fid) => {
        if (window.confirm(`آیا میخواهید پست ${fid} پاک شود؟`)) {
            try {
                await axios.delete(`http://127.0.0.1:8000/admin/fruits/${fid}/delete`);
                await fetchFruits()
            } catch (error) {
                console.error('Error deleting post:', error);
            }
        }
    }

</script>


<template>
        <Navbar></Navbar>
 
        <section class="ftco-section">
		<div class="container">
			<div class="row justify-content-center">
				<div class="col-md-6 text-center mb-4">
					<h2 class="heading-section">لیست مطالب سایت</h2>
				</div>
			</div>
			<div class="row">
				<div class="col-md-12">
					<h3 class="h5 mb-4 text-center">پست ها</h3>
                    <router-link to="/admin/create" class="btn btn-info mb-3">اضافه کردن</router-link>
					<div class="table-wrap">
						<table class="table">
						  <thead class="thead-primary">
						    <tr>
						    	<th>&nbsp;</th>
						    	<th>عنوان</th>
						    	<th>توضیحات</th>
                                <th>تاریخ</th>
						        <th class="w100">&nbsp;</th>
						    </tr>
						  </thead>
						  <tbody>
						    <tr v-for="fruit in fruits" class="alert" role="alert">
						    	<td>
						    		<div class="img-adm img" :style="{ backgroundImage: `url('/src/assets/pics/${fruit.img}')` }"></div>
						    	</td>
                                
                                <td>
						    		<p><router-link :to="getHrefUrl(fruit._id)">{{ fruit.title }}</router-link></p>
						    	</td>
						    	
						      <td>
                                <p>{{ fruit.description }}</p>
						      </td>
						      <td>{{ fruit.datetime }}</td>

						      <td>
                                <a href="#" @click="deleteFruit(fruit._id)" class="text-danger">حذف</a>
				        	</td>
						    </tr>

						  </tbody>
						</table>
					</div>
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
   .img-adm{
    width: 100px;
    height: 100px;
   }
   .w100{
    width: 100px;
   }
</style>

