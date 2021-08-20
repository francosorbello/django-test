<template>
<div>
    <ul>
        <li :key="user.id" v-for="user in users" >
            {{ user.nombre }} ({{ user.edad }})
            <button @click="onDelete($event,user)">Borrar</button>
        </li>
    </ul>
</div>
</template>

<script>
export default {
    name: "UserList",
    props: {
        users: Array,
    },
    methods: {
        onDelete(e,user) {
            this.$emit('delete-user',user)
        }
    },
}
</script>

<style>

</style>