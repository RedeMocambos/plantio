<template>
    <v-container fluid>
        <v-layout>
            <v-flex xs10>
                <v-data-table
                    :headers="header"
                    :items="especies"
                >
                    <template
                        v-slot:items="props"
                    >
                        <td>{{ props.index + 1 }}</td>
                        <td>
                            <a
                                :href="getEspecieUrl(props.item.id)">
                                {{ props.item.nome_cientifico }}
                            </a>
                        </td>
                        <td>{{ props.item.familia }}</td>
                        <td>{{ props.item.nomes_populares }}</td>
                    </template>
                </v-data-table>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'Especies',
    data() {
        return {
            header: [
                {
                    text: '#',
                    align: 'left',
                    sortable: false,
                    value: 'numero',
                },
                {
                    text: 'nome científico',
                    value: 'nome_cientifico',
                },
                {
                    text: 'família',
                    value: 'familia',
                },
                {
                    text: 'nomes populares',
                    value: 'nomes_populares',
                },
            ],
            especies: [],
        };
    },
    watch: {
        listaEspecies() {
            console.log(typeof this.listaEspecies);
            console.log(this.listaEspecies);
            this.especies = this.listaEspecies;
        },
    },
    created() {
        this.buscarEspecies();
    },
    methods: {
        ...mapActions({
            buscarEspecies: 'especie/buscarEspecies',
        }),
        getEspecieUrl(id) {
            return `especie/` + id;
        },
    },
    computed: {
        ...mapGetters({
            listaEspecies: 'especie/especies',
        }),
    },
};
</script>
