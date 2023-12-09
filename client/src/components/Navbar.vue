<script setup>
    import { ref, onMounted } from 'vue'
    import { useRouter } from 'vue-router';

    const router = useRouter();

    onMounted( () => {
        const token = localStorage.getItem('token');
        const user = JSON.parse(localStorage.getItem('user'))
        if (user && token){
            isLogin.value = true
            username.value = user.username
        }
        else{
            isLogin.value = false
        }
    });

    const logOut = () => {
        isLogin.value = false
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        router.push('/');
    }

    const username = ref('')

    const isLogin = ref(false);
  
</script>


<template>
    <!--header-->
    <div class="py-1 bg-primary">
            <div class="container">
                <div class="row no-gutters d-flex align-items-start align-items-center px-md-0">
                    <div class="col-lg-12 d-block">
                        <div class="row d-flex">
                            <div class="col-md pl-4 d-flex topper align-items-center">
                                <div class="icon ml-2 d-flex justify-content-center align-items-center"><span
                                        class="icon-phone2"></span></div>
                                <span class="text">02112345678</span>
                            </div>
                            <div class="col-md pl-4 d-flex topper align-items-center">
                                <div class="icon ml-2 d-flex justify-content-center align-items-center"><span
                                        class="icon-paper-plane"></span></div>
                                <span class="text">email@website.com</span>
                            </div>
                            <div class="col-md-5 pl-4 d-flex topper align-items-center text-lg-left">
                                <span class="text">ارسال بین 3-5 روز کاری</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!--header-->

        <!--Start Nav-->
        <nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
            <div class="container">
                <router-link to="/" class="navbar-brand">سلامت لند</router-link>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav"
                        aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="oi oi-menu"></span> منو
                </button>

                <div class="collapse navbar-collapse" id="ftco-nav">
                    <ul class="navbar-nav ml-auto">
                        <li class="nav-item active"><router-link to="/" class="nav-link">خانه</router-link></li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="dropdown04" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">دارو</a>
                            <div class="dropdown-menu" id="top-dropdown-menu" aria-labelledby="dropdown04">
                                <router-link to="/fruits" class="dropdown-item">میوه درمانی</router-link>
                                <router-link to="/medicines" class="dropdown-item">دارو گیاهی</router-link>
                            </div>
                        </li>
                        <li class="nav-item"><router-link to="/illness" class="nav-link">بیماری</router-link></li>
                        <li class="nav-item"><router-link to="/posts" class="nav-link">طب سنتی</router-link></li>
                        <li class="nav-item"><router-link to="/qa" class="nav-link">سوالات شما</router-link></li>
                        <li class="nav-item"><router-link to="/contact" class="nav-link">تماس با ما</router-link></li>
                    </ul>
                    <ul class="navbar-nav ml-left" v-if="isLogin">
                        <li class="nav-item"><router-link to="/search" class="nav-link"><span class="icon ion-ios-search"></span></router-link></li>
                        <li class="nav-item"><router-link to="/profile" class="nav-link">{{ username }}</router-link></li>
                        <li class="nav-item"><a href="#" @click="logOut" class="nav-link">خروج</a></li>
                    </ul>
                    <ul class="navbar-nav ml-left" v-else>
                        <li class="nav-item"><router-link to="/search" class="nav-link"><span class="icon ion-ios-search"></span></router-link></li>
                        <li class="nav-item"><router-link to="/login" class="nav-link">ورود</router-link></li>
                        <li class="nav-item"><router-link to="/register" class="nav-link">ثبت نام</router-link></li>
                    </ul>
                </div>
            </div>
        </nav>
        <!-- END nav -->
</template>