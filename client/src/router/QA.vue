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
            const response = await axios.get(`http://127.0.0.1:8000/qa?keyword=${keyword.value}`);
            items.value = response.data.map(splitText)
            searchTitle.value = keyword.value
        } catch (error) {
            console.error('Error searching questions:', error);
        }
    };


    const initSearch = async () => {
        const q = route.query.q
        console.log(q)
        if (q){
            keyword.value = q
            searchTitle.value = q
            await search()
        }
    }

    const splitText = (text) => {
        const parts = text.text.split('پاسخ:');
        return {
            question: parts[0].trim(),
            answer: parts[1] ? parts[1].trim() : '',
        };
    };

    const items = ref([]);
    const keyword = ref('')
    const searchTitle = ref('')

    onMounted(async () => {
        await initSearch()
        await loadMainScript()
        await LoaderScript()
    });

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
                            
                            <div v-for="item in items" class="col-md-12 d-flex">
                                <div class="blog-entry align-self-stretch d-md-flex">
                                    
                                    <div class="text d-block pr-md-4 txt-div">
                                        <p class="question">{{ item.question }}</p>
                                        <p class="answer" v-if="item.answer">پاسخ: {{ item.answer }}</p>
                                    </div>
                                    <div class="line"></div>
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
  
<style>
.txt-div{
    color:black
}
.answer{
    color:darkred
}
</style>
