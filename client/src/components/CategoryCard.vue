<script setup>
    
</script>


<template>
    <section class="ftco-section ftco-category ftco-no-pt">
            <div class="container">
                <div class="row">
                    <div class="col-md-8">
                        <div class="row">
                            <div class="col-md-6 order-md-last align-items-stretch d-flex">
                                <div class="category-wrap-2 ftco-animate img align-self-stretch d-flex"
                                    style="background-image: url(/src/assets/pics/ai.jpg);">
                                    <div class="text text-center">
                                        <h2>طب سنتی هوشمند</h2>
                                        <p>معرفی دارو برای علائم</p>
                                        <p><router-link class="btn btn-primary" to="/ai_doctor">جزییات</router-link></p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="category-wrap ftco-animate img mb-4 d-flex align-items-end"
                                    style="background-image: url(/src/assets/pics/category-1.jpg);">
                                    <div class="text px-3 py-1">
                                        <h2 class="mb-0"><router-link to="/fruits">مواد غذایی</router-link></h2>
                                    </div>
                                </div>
                                <div class="category-wrap ftco-animate img d-flex align-items-end"
                                    style="background-image: url(/src/assets/pics/illnes.webp);">
                                    <div class="text px-3 py-1">
                                        <h2 class="mb-0"><router-link to="/illness">بیماری ها</router-link></h2>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-4">
                            <div class="category-wrap ftco-animate img mb-4 d-flex align-items-end"
                                style="background-image: url(/src/assets/pics/trm.jpg);">
                                <div class="text px-3 py-1">
                                    <h2 class="mb-0"><router-link to="/medicines">دارو های گیاهی</router-link></h2>
                                </div>
                            </div>
                            <div class="category-wrap ftco-animate img d-flex align-items-end"
                                style="background-image: url(/src/assets/pics/medicine.jpg);">
                                <div class="text px-3 py-1">
                                    <h2 class="mb-0"><router-link to="/posts">دارو ها</router-link></h2>
                                </div>
                            </div>
                        </div>
                </div>
            </div>
        </section>
</template>