<script setup>
    import { ref, onMounted } from 'vue'
    import { LoaderScript, loadMainScript } from '/src/assets/js/main.js'

    import Navbar from '../components/Navbar.vue'
    import Footer from '../components/Footer.vue'
    import Loader from '../components/Loader.vue'
    import DetailHeader from '../components/DetailHeader.vue'
    import { useRoute, useRouter, onBeforeRouteUpdate, onBeforeRouteLeave  } from 'vue-router';

    import axios from 'axios'

    const route = useRoute();
    
    const fetchIllness = async () => {

        try {
            page.value = parseInt(route.query.page) || 1
            console.log(page.value)
            const response = await axios.get(`http://127.0.0.1:8000/illness?page=${page.value}`);
            illness.value = response.data.posts;
        } catch (error) {
            console.error('Error fetching posts:', error);
        }
    };

    const illness = ref([]);
    const page = ref(parseInt(route.query.page) || 1);
    const totalPages = ref(4);
    const router = useRouter();

    onMounted(async () => {
        await fetchIllness()
        await loadMainScript()
        await LoaderScript()
    });

    const getHrefUrl = (id) => {
        return `/illness/${id}`;
    };

    const prevPage = () => {
        if (page.value > 1) {
            page.value--;
            router.push({ query: { page: page.value } });
        }
    };

    const nextPage = () => {
        if (page.value < totalPages.value) {
            page.value++;
            router.push({ query: { page: page.value } });
        }
    };

    const cleanupData = () => {
        illness.value = []
    };

</script>


<template>
        <Navbar></Navbar>

        <DetailHeader img_url="/src/assets/pics/bg_1.jpg" header_title="بیماری ها"></DetailHeader>

        <section class="ftco-section ftco-degree-bg">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 ftco-animate">
                        <div class="row">
                            
                            <div v-for="illnes in illness" :key="illnes._id" class="col-md-12 d-flex ftco-animate">
                                <div class="blog-entry align-self-stretch d-md-flex">
                                    <router-link :to="getHrefUrl(illnes._id)" class="block-20"
                                     :style="{ backgroundImage: `url('/src/assets/pics/${illnes.img}')` }">
                                    </router-link>
                                    <div class="text d-block pr-md-4">
                                        <div class="meta mb-3">
                                            <div><a href="#">{{ illnes.datetime }}</a></div>
                                            <div><a href="#">کاربر</a></div>
                                            <div><a href="#" class="meta-chat"><span class="icon-chat"></span> 3</a></div>
                                        </div>
                                        <h3 class="heading"><a href="#">{{ illnes.title }}</a></h3>
                                        <p>{{ illnes.description }}</p>
                                        <p><router-link :to="getHrefUrl(illnes._id)" class="btn btn-primary py-2 px-3">بیشتر بخوانید</router-link>
                                        </p>
                                    </div>
                                </div>
                            </div>
                            
                        </div>
                    </div> <!-- .col-md-8 -->
                    <!-- Sidebar-->
                    <div class="col-lg-4 sidebar ftco-animate">
                        <div class="sidebar-box">
                            <form action="#" class="search-form">
                                <div class="form-group">
                                    <span class="icon ion-ios-search"></span>
                                    <input type="text" class="form-control" placeholder="جست و جو...">
                                </div>
                            </form>
                        </div>
                        <div class="sidebar-box ftco-animate">
                            <h3 class="heading">محصولات</h3>
                            <ul class="categories">
                                <li><a href="#">سبزیجات <span>(12)</span></a></li>
                                <li><a href="#">میوه <span>(22)</span></a></li>
                                <li><a href="#">آبمیوه <span>(37)</span></a></li>
                                <li><a href="#">میوه خشک <span>(42)</span></a></li>
                            </ul>
                        </div>

                        <div class="sidebar-box ftco-animate">
                            <h3 class="heading">آخرین پست ها</h3>
                            <div class="block-21 mb-4 d-flex">
                                <a class="blog-img ml-4" style="background-image: url(/src/assets/pics/image_1.jpg);"></a>
                                <div class="text">
                                    <h3 class="heading-1"><a href="#">غذاهای ارگانیک عبارتند از غذاهای حیوانی و گیاهی که در
                                        تولید آن از سیستم های طبیعی استفاده شده</a></h3>
                                    <div class="meta">
                                        <div><a href="#"><span class="icon-calendar"></span> 28 بهمن ۱۳۹۸</a></div>
                                        <div><a href="#"><span class="icon-person"></span> کاربر</a></div>
                                        <div><a href="#"><span class="icon-chat"></span> 19</a></div>
                                    </div>
                                </div>
                            </div>
                            <div class="block-21 mb-4 d-flex">
                                <a class="blog-img ml-4" style="background-image: url(/src/assets/pics/image_2.jpg);"></a>
                                <div class="text">
                                    <h3 class="heading-1"><a href="#">غذاهای ارگانیک عبارتند از غذاهای حیوانی و گیاهی که در
                                        تولید آن از سیستم های طبیعی استفاده شده</a></h3>
                                    <div class="meta">
                                        <div><a href="#"><span class="icon-calendar"></span> 28 بهمن ۱۳۹۸</a></div>
                                        <div><a href="#"><span class="icon-person"></span> کاربر</a></div>
                                        <div><a href="#"><span class="icon-chat"></span> 19</a></div>
                                    </div>
                                </div>
                            </div>
                            <div class="block-21 mb-4 d-flex">
                                <a class="blog-img ml-4" style="background-image: url(/src/assets/pics/image_3.jpg);"></a>
                                <div class="text">
                                    <h3 class="heading-1"><a href="#">غذاهای ارگانیک عبارتند از غذاهای حیوانی و گیاهی که در
                                        تولید آن از سیستم های طبیعی استفاده شده</a></h3>
                                    <div class="meta">
                                        <div><a href="#"><span class="icon-calendar"></span> 28 بهمن ۱۳۹۸</a></div>
                                        <div><a href="#"><span class="icon-person"></span> کاربر</a></div>
                                        <div><a href="#"><span class="icon-chat"></span> 19</a></div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="sidebar-box ftco-animate">
                            <h3 class="heading">لیست محصولات موجود</h3>
                            <div class="tagcloud">
                                <a href="#" class="tag-cloud-link">میوه</a>
                                <a href="#" class="tag-cloud-link">گوجه</a>
                                <a href="#" class="tag-cloud-link">مانجو</a>
                                <a href="#" class="tag-cloud-link">سیب</a>
                                <a href="#" class="tag-cloud-link">هویج</a>
                                <a href="#" class="tag-cloud-link">پرتغال</a>
                                <a href="#" class="tag-cloud-link">فلفل</a>
                                <a href="#" class="tag-cloud-link">بادمجون</a>
                            </div>
                        </div>

                        <div class="sidebar-box ftco-animate">
                            <h3 class="heading">محصولات ارگانیک</h3>
                            <p>غذاهای ارگانیک عبارتند از غذاهای حیوانی و گیاهی که در تولید آن از سیستم های طبیعی استفاده
                                شده</p>
                        </div>
                    </div>

                </div>
            </div>
        </section>
        <!-- End section -->     

        <!-- <button class="btn btn-primary" @click="prevPage" :disabled="page === 1">Previous</button>
        <button class="btn btn-primary" @click="nextPage" :disabled="page === totalPages">Next</button> -->

        <Footer></Footer>

        <Loader></Loader>

</template>
  
