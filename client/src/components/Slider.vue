<template>
    <!--Start Slider-->
    <section id="home-section" class="hero">
            <div class="home-slider owl-carousel">
                <div class="slider-item" style="background-image: url(/src/assets/pics/bg_1.jpg);">
                    <div class="overlay"></div>
                    <div class="container">
                        <div class="row slider-text justify-content-center align-items-center" data-scrollax-parent="true">

                            <div class="col-md-12 ftco-animate text-center">
                                <h1 class="mb-2">دارو ها و معرفی محصولات گیاهی</h1>
                                <h2 class="subheading mb-4">میوه و سبزیجات برای رفع بیماری</h2>
                                <p><router-link to="/medicines" class="btn btn-primary">مشاهده جزییات</router-link></p>
                            </div>

                        </div>
                    </div>
                </div>

                <div class="slider-item" style="background-image: url(/src/assets/pics/trm2.jpg);">
                    <div class="overlay"></div>
                    <div class="container">
                        <div class="row slider-text justify-content-center align-items-center" data-scrollax-parent="true">

                            <div class="col-sm-12 ftco-animate text-center">
                                <h1 class="mb-2">طب سنتی هوشمند</h1>
                                <h2 class="subheading mb-4">درمان بیماری ها با طب سنتی</h2>
                                <p><router-link to="/posts" class="btn btn-primary">مشاهده جزییات</router-link></p>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!--End Slider-->
</template>