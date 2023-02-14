<script setup>
import { useRouter } from "vue-router";
const props = defineProps(['list',])
const router = useRouter()

const back = (index) => {
    if(index == 0)
        router.push("/");
    };
</script>

<template>
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb ">
            <li role="button" class="breadcrumb-item" > <a href="https://www.inferia.io/"> Inicio</a></li>
            <li role="button" class="breadcrumb-item" v-for="(item, index) in props.list" :key="index" @click="back(index)"> <a> {{ item }}</a></li>
        </ol>
    </nav>
</template>