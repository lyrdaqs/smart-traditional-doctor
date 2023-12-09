<script setup>
    const props = defineProps({
        header_title: String,
        img_url: String
    })
    
</script>

<template>
    <div class="hero-wrap hero-bread" :style="{backgroundImage: `url(${img_url})`}">
            <div class="container">
                <div class="row no-gutters slider-text align-items-center justify-content-center">
                    <div class="col-md-9 ftco-animate text-center">
                        <p class="breadcrumbs"><span class="ml-2"><a href="index.html">خانه</a></span></p>
                        <h1 class="mb-0 bread">{{ header_title }}</h1>
                    </div>
                </div>
            </div>
        </div>
</template>