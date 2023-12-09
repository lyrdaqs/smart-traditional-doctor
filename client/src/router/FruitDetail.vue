<script setup>
    import { ref, onMounted } from 'vue'
    import { LoaderScript, loadMainScript } from '/src/assets/js/main.js'

    import Navbar from '../components/Navbar.vue'
    import Footer from '../components/Footer.vue'
    import Loader from '../components/Loader.vue'
    import { useRoute } from 'vue-router';

    import axios from 'axios'

    const route = useRoute();

    const fetchFruit = async () => {
        try {
            const fruitId = route.params.id;
            const response = await axios.get(`http://127.0.0.1:8000/fruits/${fruitId}`);
            fruit.value = response.data;
            htmlContent.value = response.data.entry_content;
        } catch (error) {
            console.error('Error fetching posts:', error);
        }
    };

    const fruit = ref([]);
    const htmlContent = ref('');
    const comment = ref('')
    const error = ref(false)
    const isLogin = ref(false)

    onMounted(async () => {
        await fetchFruit()
        getIsLogin()
        await loadMainScript()
        await LoaderScript()
    });

    const getImageUrl = (img) => {
        return `/src/assets/pics/${img}`;
    };

    const getIsLogin = () => {
        const token = localStorage.getItem('token');
        const user = JSON.parse(localStorage.getItem('user'))
        if (user && token){
            isLogin.value = true
        }
        else{
            isLogin.value = false
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

    const addComment = async () => {
        try {
            setToken()
            const fruitId = route.params.id; 
            await axios.post(`http://127.0.0.1:8000/fruits/${fruitId}/comments/add`, {"content": comment.value});
            comment.value = ""
            await fetchFruit()
        } catch (err) {
            console.error('Error comment in post:', err)
            if(err.response.status == 401){
                error.value = true
            }
        }
    } 

    const getHrefTag = (tag) => {
        return `/search?tag=${tag}`
    }

</script>


<template>
        <Navbar></Navbar>

        <section class="ftco-section ftco-degree-bg">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 ftco-animate">
                        <h2 class="mb-3">{{ fruit.title }}</h2>
                        <p>
                            <img :src="getImageUrl(fruit.img_detail)" alt="" class="img-fluid">
                        </p>
                        <div v-html="htmlContent"></div>

                        <p v-for="img in fruit.img_detail_items">
                            <img :src="getImageUrl(img)" alt="" class="img-fluid">
                        </p>

                        <div class="tag-widget post-tag-container mb-5 mt-5">
                            <div class="tagcloud">
                                <router-link :to="getHrefTag(tag)" v-for="tag in fruit.tags" class="tag-cloud-link">{{ tag }}</router-link>
                            </div>
                        </div>
                        <div class="about-author d-flex p-4 bg-light">
                            <div class="bio align-self-md-center ml-4">
                                <img src="/src/assets/pics/person_1.jpg" alt="Image placeholder" class="img-fluid mb-4">
                            </div>
                            <div class="desc align-self-md-center">
                                <h3>محمد منفرد</h3>
                                <p>اولین خوراکی ارائه شده به ما (amuse bouche) بود که بسیار اشتها آور و خوش منظره بود؛ این غذا
                                    از صدف و گوشت ماهی به شکل خمیر خامه ای تهیه شده و در یک فنجان ظریف سرو می شد.</p>
                            </div>
                        </div>
                        <div class="pt-5 mt-5">
                            <h3 class="mb-5">نظرات</h3>
                            <ul class="comment-list">
                                
                                <li class="comment" v-for="comment in fruit.comments">
                                    <div class="vcard bio">
                                        <img src="/src/assets/pics/person_1.jpg" alt="Image placeholder">
                                    </div>
                                    <div class="comment-body">
                                        <h3>{{ comment.username }}</h3>
                                        <div class="meta">{{ comment.timestamp }}</div>
                                        <p> {{ comment.content }}

                                        </p>
                                        <p><a href="#" class="reply">پاسخ</a></p>
                                    </div>
                                </li>

  
                            </ul>
                            <!-- END comment-list -->
                            
                            <div v-if="isLogin" class="comment-form-wrap pt-5">
                                <h3 class="mb-5">تجربه خود را با ما در میان بگذارید</h3>
                                <form @submit.prevent="addComment" class="p-5 bg-light">
                                    <div class="form-group">
                                        <label for="message">پیام</label>
                                        <textarea v-model="comment" id="message" cols="30" rows="10" class="form-control"></textarea>
                                    </div>
                                    <p v-if="error">توکن شما منقضی شده است دوباره <router-link to="/login">وارد</router-link> سایت شوید</p>
                                    <div class="form-group">
                                        <input type="submit" value="ارسال نظر" class="btn py-3 px-4 btn-primary">
                                    </div>
                                </form>
                            </div>
                            <div v-else>
                                <p>برای  نطر گذاشتن ایتدا باید <router-link to="/login">وارد</router-link> سایت شوید</p>
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
                            <p>غذاهای ارگانیک عبارتند از غذاهای حیوانی و گیاهی که در تولید آن از سیستم های طبیعی استفاده شده</p>
                        </div>
                    </div>

                </div>
            </div>
        </section> <!-- End section -->

        

        <Footer></Footer>

        <Loader></Loader>

</template>
  
