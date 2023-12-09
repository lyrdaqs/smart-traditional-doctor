<script setup>
    import { ref, onMounted } from 'vue'
    import { LoaderScript, loadMainScript } from '/src/assets/js/main.js'

    import Navbar from '../components/Navbar.vue'
    import Slider from '../components/Slider.vue'
    import Tozihat from '../components/Tozihat.vue'
    import CategoryCard from '../components/CategoryCard.vue'
    import Footer from '../components/Footer.vue'
    import Banner from '../components/Banner.vue'
    import Loader from '../components/Loader.vue'
    import Nazarsanji from '../components/Nazarsanji.vue'

    onMounted( async () => {
        await loadMainScript()
        await LoaderScript()
        console.log("loaded")
    });

</script>


<template>
        <Navbar></Navbar>

        <Slider></Slider>        

        <Tozihat></Tozihat>

        <CategoryCard></CategoryCard>

        <section class="ftco-section">
            <div class="container">
                <div class="row justify-content-center mb-3 pb-3">
                    <div class="col-md-12 heading-section text-center ftco-animate">
                        <span class="subheading"> انتخاب هوشمند محصولات ارگانیک</span>
                        <h2 class="mb-4">سرزمین میوه</h2>
                        <p>پیشنهاد ما به شما</p>
                    </div>
                </div>
            </div>
            <div class="container">
                <div class="row">
                    <div class="col-md-6 col-lg-3 ftco-animate">
                        <div class="product">
                            <a href="#" class="img-prod"><img class="img-fluid" src="/src/assets/pics/product-1.jpg" alt="Colorlib Template">
                                <div class="overlay"></div>
                            </a>
                            <div class="text py-3 pb-4 px-3 text-center">
                                <h3><a href="#">فلفل دلمه ای</a></h3>
                                <div class="d-flex">
                                    <div class="pricing">
                                        <p class="price">
                                            <span>1200</span>
                                            <span> پیشنهاد</span>
                                        </p>
                                    </div>
                                </div>
                                <div class="bottom-area d-flex px-3">
                                    <div class="m-auto d-flex">
                                        <a href="#"
                                        class="add-to-cart d-flex justify-content-center align-items-center text-center">
                                            <span><i class="ion-ios-menu"></i></span>
                                        </a>
                                        <a href="#" class="heart d-flex justify-content-center align-items-center ">
                                            <span><i class="ion-ios-heart"></i></span>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-3 ftco-animate">
                        <div class="product">
                            <a href="#" class="img-prod"><img class="img-fluid" src="/src/assets/pics/product-2.jpg" alt="Colorlib Template">
                                <div class="overlay"></div>
                            </a>
                            <div class="text py-3 pb-4 px-3 text-center">
                                <h3><a href="#"> توت فرنگی</a></h3>
                                <div class="d-flex">
                                    <div class="pricing">
                                        <p class="price">
                                            <span> 120</span>
                                            <span> پیشنهاد</span>
                                        </p>
                                    </div>
                                </div>
                                <div class="bottom-area d-flex px-3">
                                    <div class="m-auto d-flex">
                                        <a href="#" class="add-to-cart d-flex justify-content-center align-items-center text-center">
                                            <span><i class="ion-ios-menu"></i></span>
                                        </a>

                                        <a href="#" class="heart d-flex justify-content-center align-items-center ">
                                            <span><i class="ion-ios-heart"></i></span>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-3 ftco-animate">
                        <div class="product">
                            <a href="#" class="img-prod"><img class="img-fluid" src="/src/assets/pics/product-3.jpg" alt="Colorlib Template">
                                <div class="overlay"></div>
                            </a>
                            <div class="text py-3 pb-4 px-3 text-center">
                                <h3><a href="#">لوبیا سبز</a></h3>
                                <div class="d-flex">
                                    <div class="pricing">
                                        <p class="price">
                                            <span> 120</span>
                                            <span> پیشنهاد</span>
                                        </p>
                                    </div>
                                </div>
                                <div class="bottom-area d-flex px-3">
                                    <div class="m-auto d-flex">
                                        <a href="#"
                                        class="add-to-cart d-flex justify-content-center align-items-center text-center">
                                            <span><i class="ion-ios-menu"></i></span>
                                        </a>
                                        <a href="#" class="heart d-flex justify-content-center align-items-center ">
                                            <span><i class="ion-ios-heart"></i></span>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-3 ftco-animate">
                        <div class="product">
                            <a href="#" class="img-prod"><img class="img-fluid" src="/src/assets/pics/product-4.jpg" alt="Colorlib Template">
                                <div class="overlay"></div>
                            </a>
                            <div class="text py-3 pb-4 px-3 text-center">
                                <h3><a href="#">کلم بنفش</a></h3>
                                <div class="d-flex">
                                    <div class="pricing">
                                        <p class="price">
                                            <span>120</span>
                                            <span> پیشنهاد</span>
                                        </p>
                                    </div>
                                </div>
                                <div class="bottom-area d-flex px-3">
                                    <div class="m-auto d-flex">
                                        <a href="#"
                                        class="add-to-cart d-flex justify-content-center align-items-center text-center">
                                            <span><i class="ion-ios-menu"></i></span>
                                        </a>
                                        <a href="#" class="heart d-flex justify-content-center align-items-center ">
                                            <span><i class="ion-ios-heart"></i></span>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-6 col-lg-3 ftco-animate">
                        <div class="product">
                            <a href="#" class="img-prod"><img class="img-fluid" src="/src/assets/pics/product-5.jpg"
                                                            alt="Colorlib Template">
                                <div class="overlay"></div>
                            </a>
                            <div class="text py-3 pb-4 px-3 text-center">
                                <h3><a href="#">گوجه فرنگی</a></h3>
                                <div class="d-flex">
                                    <div class="pricing">
                                        <p class="price">
                                            <span>120</span>
                                            <span> پیشنهاد</span>
                                        </p>
                                    </div>
                                </div>
                                <div class="bottom-area d-flex px-3">
                                    <div class="m-auto d-flex">
                                        <a href="#"
                                        class="add-to-cart d-flex justify-content-center align-items-center text-center">
                                            <span><i class="ion-ios-menu"></i></span>
                                        </a>
                                        <a href="#" class="heart d-flex justify-content-center align-items-center ">
                                            <span><i class="ion-ios-heart"></i></span>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-3 ftco-animate">
                        <div class="product">
                            <a href="#" class="img-prod"><img class="img-fluid" src="/src/assets/pics/product-6.jpg" alt="Colorlib Template">
                                <div class="overlay"></div>
                            </a>
                            <div class="text py-3 pb-4 px-3 text-center">
                                <h3><a href="#">کلم بروکلی</a></h3>
                                <div class="d-flex">
                                    <div class="pricing">
                                        <p class="price">
                                            <span>120</span>
                                            <span> پیشنهاد</span>
                                        </p>
                                    </div>
                                </div>
                                <div class="bottom-area d-flex px-3">
                                    <div class="m-auto d-flex">
                                        <a href="#"
                                        class="add-to-cart d-flex justify-content-center align-items-center text-center">
                                            <span><i class="ion-ios-menu"></i></span>
                                        </a>

                                        <a href="#" class="heart d-flex justify-content-center align-items-center ">
                                            <span><i class="ion-ios-heart"></i></span>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-3 ftco-animate">
                        <div class="product">
                            <a href="#" class="img-prod"><img class="img-fluid" src="/src/assets/pics/product-7.jpg" alt="Colorlib Template">
                                <div class="overlay"></div>
                            </a>
                            <div class="text py-3 pb-4 px-3 text-center">
                                <h3><a href="#">هویج</a></h3>
                                <div class="d-flex">
                                    <div class="pricing">
                                        <p class="price">
                                            <span>120</span>
                                            <span> پیشنهاد</span>
                                        </p>
                                    </div>
                                </div>
                                <div class="bottom-area d-flex px-3">
                                    <div class="m-auto d-flex">
                                        <a href="#"
                                        class="add-to-cart d-flex justify-content-center align-items-center text-center">
                                            <span><i class="ion-ios-menu"></i></span>
                                        </a>
            
                                        <a href="#" class="heart d-flex justify-content-center align-items-center ">
                                            <span><i class="ion-ios-heart"></i></span>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-3 ftco-animate">
                        <div class="product">
                            <a href="#" class="img-prod"><img class="img-fluid" src="/src/assets/pics/product-8.jpg"
                                                            alt="Colorlib Template">
                                <div class="overlay"></div>
                            </a>
                            <div class="text py-3 pb-4 px-3 text-center">
                                <h3><a href="#">آبمیوه های طبیعی</a></h3>
                                <div class="d-flex">
                                    <div class="pricing">
                                        <p class="price">
                                            <span>120</span>
                                            <span> پیشنهاد</span>
                                        </p>
                                    </div>
                                </div>
                                <div class="bottom-area d-flex px-3">
                                    <div class="m-auto d-flex">
                                        <a href="#"
                                        class="add-to-cart d-flex justify-content-center align-items-center text-center">
                                            <span><i class="ion-ios-menu"></i></span>
                                        </a>
        
                                        <a href="#" class="heart d-flex justify-content-center align-items-center ">
                                            <span><i class="ion-ios-heart"></i></span>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <Banner></Banner>
        
        <Nazarsanji></Nazarsanji>

        <hr>

        <section class="ftco-section ftco-partner">
            <div class="container">
                <div class="row">
                    <div class="col-sm ftco-animate">
                        <a href="#" class="partner"><img src="/src/assets/pics/partner-1.png" class="img-fluid"
                                                        alt="Colorlib Template"></a>
                    </div>
                    <div class="col-sm ftco-animate">
                        <a href="#" class="partner"><img src="/src/assets/pics/partner-2.png" class="img-fluid"
                                                        alt="Colorlib Template"></a>
                    </div>
                    <div class="col-sm ftco-animate">
                        <a href="#" class="partner"><img src="/src/assets/pics/partner-3.png" class="img-fluid"
                                                        alt="Colorlib Template"></a>
                    </div>
                    <div class="col-sm ftco-animate">
                        <a href="#" class="partner"><img src="/src/assets/pics/partner-4.png" class="img-fluid"
                                                        alt="Colorlib Template"></a>
                    </div>
                    <div class="col-sm ftco-animate">
                        <a href="#" class="partner"><img src="/src/assets/pics/partner-5.png" class="img-fluid"
                                                        alt="Colorlib Template"></a>
                    </div>
                </div>
            </div>
        </section>

        <Footer></Footer>

        <Loader></Loader>

</template>
  
