<script setup>
    import { ref, onMounted } from 'vue'
    import { LoaderScript, loadMainScript } from '/src/assets/js/main.js'

    import Navbar from '../components/Navbar.vue'
    import Footer from '../components/Footer.vue'
    import Loader from '../components/Loader.vue'

    import axios from 'axios'
    import { useRoute } from 'vue-router';

    const route = useRoute()
    
    const search = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/search?keyword=${keyword.value}`);
            items.value = response.data;
            searchTitle.value = keyword.value
        } catch (error) {
            console.error('Error searching posts:', error);
        }
    };

    const get_tag_items = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/get_items_by_tag?tag=${keyword.value}`);
            items.value = response.data;
            searchTitle.value = keyword.value
        } catch (error) {
            console.error('Error searching posts:', error);
        }
    };

    const initSearch = async () => {
        const tag = route.query.tag
        console.log(tag)
        if (tag){
            keyword.value = tag
            searchTitle.value = tag
            await get_tag_items()
        }
        const q = route.query.q
        console.log(q)
        if (q){
            keyword.value = q
            searchTitle.value = q
            await search()
        }
    }

    const items = ref([]);
    const keyword = ref('')
    const searchTitle = ref('')

    onMounted(async () => {
        await initSearch()
        await loadMainScript()
        await LoaderScript()
    });

    const getHrefUrl = (id, role) => {
        if(role=="fruit")
            return `/fruits/${id}`;
        else if(role=="medicine")
            return `/medicines/${id}`;
        else if(role=="illnes")
            return `/illness/${id}`;
        else
            return `/posts/${id}`;
    };

</script>


<template>
        <Navbar></Navbar>

        <div class="hero-wrap hero-bread" :style="{backgroundImage: 'url(/src/assets/pics/bg_1.jpg)'}">
            <div class="container">
                <div class="row no-gutters slider-text align-items-center justify-content-center">
                    <div class="col-md-9 ftco-animate text-center">
                        <p class="breadcrumbs"><span class="ml-2"><a href="index.html">خانه</a></span></p>
                        <div class="sidebar-box">
                            <form @submit.prevent="search" class="search-form">
                                <div class="form-group">
                                    <span class="icon ion-ios-search"></span>
                                    <input v-model="keyword" type="text" class="form-control" placeholder="جست و جو...">
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>


        <section class="ftco-section ftco-degree-bg">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 ftco-animate">
                        <div class="mb-5">
                            <h2>کلمه جستجو شده: {{ searchTitle }}</h2>
                        </div>
                        <div class="row">
                            
                            <div v-for="item in items" :key="item.store_id" class="col-md-12 d-flex">
                                <div class="blog-entry align-self-stretch d-md-flex">
                                    <router-link :to="getHrefUrl(item.store_id, item.role)" class="block-20"
                                     :style="{ backgroundImage: `url('/src/assets/pics/${item.img}')` }">
                                    </router-link>
                                    <div class="text d-block pr-md-4">
                                        <h3 class="heading"><a href="#">{{ item.title }}</a></h3>
                                        <p>{{ item.description }}</p>
                                        <p><router-link :to="getHrefUrl(item.store_id, item.role)" class="btn btn-primary py-2 px-3">بیشتر بخوانید</router-link>
                                        </p>
                                    </div>
                                </div>
                            </div>
                            
                        </div>
                    </div> <!-- .col-md-8 -->
             

                </div>
            </div>
        </section>
        <!-- End section -->     

        

        <Footer></Footer>

        <Loader></Loader>

</template>
  
